/*
 * Instituto TecnolÃ³gico de Costa Rica
 * Computer Engineering
 * Taller de ProgramaciÃ³n
 * 
 * Código Servidor
 * Implementación del servidor NodeMCU
 * Proyecto 2, semestre 1
 * 2019
 * 
 * Profesor: Milton Villegas Lemus
 * Autor: Santiago Gamboa RamÃ­rez
 * 
 * Restricciónes: Biblioteca ESP8266WiFi instalada
 */
#include <ESP8266WiFi.h>

//Cantidad maxima de clientes es 1
#define MAX_SRV_CLIENTS 1
//Puerto por el que escucha el servidor
#define PORT 7070

/*
 * ssid: Nombre de la Red a la que se va a conectar el Arduino
 * password: Contraseña de la red
 * 
 * Este servidor no funciona correctamente en las redes del TEC,
 * se recomienda crear un hotspot con el celular
 */
const char* ssid = "HUAWEI";
const char* password = "11235813";


// servidor con el puerto y variable con la maxima cantidad de 

WiFiServer server(PORT);
WiFiClient serverClients[MAX_SRV_CLIENTS];

/*
 * Intervalo de tiempo que se espera para comprobar que haya un nuevo mensaje
 */
unsigned long previousMillis = 0, temp = 0;
const long interval = 100;

/*
 * Pin donde está conectado el sensor de luz
 * Señal digital, lee 1 si hay luz y 0 si no hay.
 */
#define ldr D7
/**
 * Variables para manejar las luces con el registro de corrimiento.
 * Utilizan una función propia de Arduino llamada shiftOut.
 * shiftOut(ab,clk,LSBFIRST,data), la función recibe 2 pines, el orden de los bits 
 * y un dato de 8 bits.
 * El registro de corrimiento tiene 8 salidas, desde QA a QH. Nosotros usamos 6 de las 8 salidas
 * Ejemplos al enviar data: 
 * data = B00000000 -> todas encendidas
 * data = B11111111 -> todas apagadas
 * data = B00001111 -> depende de LSBFIRST o MSBFIRST la mitad encendida y la otra mitad apagada
 */
#define ab  D6 
#define clk D8
/*
 * Variables para controlar los motores.
 * EnA y EnB son los que habilitan las salidas del driver.
 * EnA = 0 o EnB = 0 -> free run (No importa que haya en las entradas el motor no recibe potencia)
 * EnA = 0 -> Controla la potencia (Para regular la velocidad utilizar analogWrite(EnA,valor), 
 * con valor [0-1023])
 * EnB = 0 -> Controla la dirección, poner en 0 para avanzar directo.
 * In1 e In2 son inputs de driver, controlan el giro del motor de potencia
 * In1 = 0 ∧ In2 = 1 -> Moverse hacia adelante
 * In1 = 1 ∧ In2 = 0 -> Moverse en reversa
 * In3 e In4 son inputs de driver, controlan la dirección del carro
 * In3 = 0 ∧ In4 = 1 -> Gira hacia la izquierda
 * In3 = 1 ∧ In4 = 0 -> Gira hacia la derecha
 */
#define EnA D4 // 
#define In1 D3 // D4 en HIGH : retroceder
#define In2 D2 // D3 en HIGH : avanzar
#define In3 D1 // 
#define EnB D5 // 
#define In4 D0 //
#define bat A0 //
// 0 para ir hacia adelante



/**
 * Variables
 */
// #AGREGAR VARIABLES NECESARIAS 

/**
 * Función de configuración.
 * Se ejecuta la primera vez que el módulo se enciende.
 * Si no puede conectarse a la red especificada entra en un ciclo infinito 
 * hasta ser reestablecido y volver a llamar a la función de setup.
 * La velocidad de comunicación serial es de 115200 baudios, tenga presente
 * el valor para el monitor serial.
 */
void setup() {
  Serial.begin(115200);
  pinMode(In1,OUTPUT);
  pinMode(In2,OUTPUT);
  pinMode(In3,OUTPUT);
  pinMode(In4,OUTPUT);
  pinMode(EnA,OUTPUT);
  pinMode(EnB,OUTPUT);
  pinMode(clk,OUTPUT);
  pinMode(ab,OUTPUT);
  
  pinMode(ldr,INPUT);

  // ip estática para el servidor
  IPAddress ip(192,168,43,200);
  IPAddress gateway(192,168,43,1);
  IPAddress subnet(255,255,255,0);

  WiFi.config(ip, gateway, subnet);

  // Modo para conectarse a la red
  WiFi.mode(WIFI_STA);
  // Intenta conectar a la red
  WiFi.begin(ssid, password);
  
  uint8_t i = 0;
  while (WiFi.status() != WL_CONNECTED && i++ < 20) delay(500);
  if (i == 21) {
    Serial.print("\nCould not connect to: "); Serial.println(ssid);
    while (1) delay(500);
  } else {
    Serial.print("\nConnection Succeeded to: "); Serial.println(ssid);
    Serial.println(".....\nWaiting for a client at");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
    Serial.print("Port: ");
    Serial.print(PORT);
  }
  server.begin();
  server.setNoDelay(true);




}

/*
 * Función principal que llama a las otras funciones y recibe los mensajes del cliente
 * Esta función comprueba que haya un nuevo mensaje y llama a la función de procesar
 * para interpretar el mensaje recibido.
 */

byte data= 0b11111111;
int Diz=0;
int Dde=0;
int fr=0;
int tra=0;
float voltage = 0;
int analogV = 0;
int vv = 0;
int resuB = 0;
String bate = "nivel de bateria: " ;
int r = 0;
int foto = 0;
void loop() {
  
  unsigned long currentMillis = millis();
  uint8_t i;
  //check if there are any new clients
  if (server.hasClient()) {
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      //find free/disconnected spot
      if (!serverClients[i] || !serverClients[i].connected()) {
        if (serverClients[i]) serverClients[i].stop();
        serverClients[i] = server.available();
        continue;
      }
    }
    //no free/disconnected spot so reject
    WiFiClient serverClient = server.available();
    serverClient.stop();
  }

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    for (i = 0; i < MAX_SRV_CLIENTS; i++) {
      // El cliente existe y está conectado
      if (serverClients[i] && serverClients[i].connected()) {
        // El cliente tiene un nuevo mensaje
        if(serverClients[i].available()){
          // Leemos el cliente hasta el caracter '\r'
          String mensaje = serverClients[i].readStringUntil('\r');
          // Eliminamos el mensaje leído.
          serverClients[i].flush();
          
          // Preparamos la respuesta para el cliente
          String respuesta; 
          procesar(mensaje, &respuesta);
          Serial.println(mensaje);
          // Escribimos la respuesta al cliente.
          serverClients[i].println(respuesta);
        }  
        serverClients[i].stop();
      }
    }
  }
}

/*
 * Función para dividir los comandos en pares llave, valor
 * para ser interpretados y ejecutados por el Carro
 * Un mensaje puede tener una lista de comandos separados por ;
 * Se analiza cada comando por separado.
 * Esta función es semejante a string.split(char) de python
 * 
 */
void procesar(String input, String * output){
  //Buscamos el delimitador ;
  Serial.println("Checking input....... ");
  int comienzo = 0, delComa, del2puntos;
  bool result = false;
  delComa = input.indexOf(';',comienzo);
  
  while(delComa>0){
    String comando = input.substring(comienzo, delComa);
    Serial.print("Processing comando: ");
    Serial.println(comando);
    del2puntos = comando.indexOf(':');
    /*
    * Si el comando tiene ':', es decir tiene un valor
    * se llama a la función exe 
    */
    if(del2puntos>0){
        String llave = comando.substring(0,del2puntos);
        String valor = comando.substring(del2puntos+1);

        Serial.print("(llave, valor) = ");
        Serial.print(llave);
        Serial.println(valor);
        //Una vez separado en llave valor 
        *output = implementar(llave,valor); 
    }
    else if(comando == "sense"){
      *output = getSense();         
    }
    else if(comando == "bate"){
      *output = getBate();}

    else if(comando == "zig"){
      digitalWrite (In1,HIGH);
      digitalWrite (In2,LOW);
      analogWrite (EnA,1023);
      result = "adelante";
      digitalWrite (In3,HIGH);
      digitalWrite (In4,LOW);
      analogWrite(EnB,1023);
      delay(2000);
      result="izquierda";
      /*digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(3000);
      result="directo";**/
      digitalWrite (In3,LOW);
      digitalWrite (In4,HIGH);
      analogWrite(EnB,1000);
      delay(2000);
      result = "derecha";
      /*digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(3000);**/
      result="directo";
      digitalWrite (In3,HIGH);
      digitalWrite (In4,LOW);
      analogWrite(EnB,1000);
      delay(1700);
      result="izquierda";
      /*digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(3000);
      result="directo";*/
      digitalWrite (In3,LOW);
      digitalWrite (In4,HIGH);
      analogWrite(EnB,1000);
      result = "derecha";
      delay(1500);
      digitalWrite (In1,LOW);
      digitalWrite (In2,LOW);
      analogWrite (EnA,0);
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      result = "detenido";
    }

    else if(comando=="cir"){
      digitalWrite (In3,HIGH);
      digitalWrite (In4,LOW);
      analogWrite(EnB,1000);
      digitalWrite (In1,HIGH);
      digitalWrite (In2,LOW);
      analogWrite (EnA,1023);
      delay(9000);
      result="circulo a la izquierda";
      digitalWrite (In1,LOW);
      digitalWrite (In2,LOW);
      analogWrite (EnA,0);
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      result = "detenido";
      
    }

    else if(comando=="inf"){
      digitalWrite (In1,HIGH);
      digitalWrite (In2,LOW);
      analogWrite (EnA,1023);
      result="avanza";
      digitalWrite (In3,LOW);
      digitalWrite (In4,HIGH);
      analogWrite(EnB,1023);
      delay(7000);
      result="derecha";
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(1000);
      result="directo";
      digitalWrite (In3,HIGH);
      digitalWrite (In4,LOW);
      analogWrite(EnB,1023);
      delay(7000);
      result="izquierda";
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(500);
      result="directo";
      digitalWrite (In3,LOW);
      digitalWrite (In4,HIGH);
      analogWrite(EnB,1023);
      delay(3000);
      result="derecha";
      
      digitalWrite (In1,LOW);
      digitalWrite (In2,LOW);
      analogWrite (EnA,0);
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
    }
    else if(comando=="esp"){
      digitalWrite (In1,HIGH);
      digitalWrite (In2,LOW);
      analogWrite (EnA,1023);
      result="avanza";
      digitalWrite (In3,HIGH);
      digitalWrite (In4,LOW);
      analogWrite(EnB,1023);
      delay(6000);
      result="izquierda";
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(500);
      result="directo";
      digitalWrite (In3,LOW);
      digitalWrite (In4,HIGH);
      analogWrite(EnB,1023);
      delay(5000);
      result="derecha";
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(2000);
      result="directo";
      digitalWrite (In3,HIGH);
      digitalWrite (In4,LOW);
      analogWrite(EnB,1023);
      delay(4000);
      result="izquierda";
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite (EnB,0);
      delay(2000);
      result="directo";
      digitalWrite (In3,LOW);
      digitalWrite (In4,HIGH);
      analogWrite(EnB,1023);
      delay(6000);
      result="derecha";
      digitalWrite (In1,LOW);
      digitalWrite (In2,LOW);
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      result="detenido";
      
      

      
    }
    
    else if(comando=="det"){
      digitalWrite (In1,LOW);
      digitalWrite (In2,LOW);
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      result="detenido";
      
      
      }
    /**
     * ## AGREGAR COMPARACIONES PARA COMANDOS SIN VALOR
     * EJEM: else if (comando == CIRCLE) {
     *  
     * } 
     */
    else{
      Serial.print("Comando no reconocido. Solo presenta llave");
      *output = "Undefined key value: " + comando+";";
    }
    comienzo = delComa+1;
    delComa = input.indexOf(';',comienzo);
  }
}

String implementar(String llave, String valor){
   int y=0;
  /**
   * La variable result puede cambiar para beneficio del desarrollador
   * Si desea obtener más información al ejecutar un comando.
   */
  String result="ok;";
  Serial.print("Comparing llave: ");
  Serial.println(llave);
  
  if(llave == "pwm"){

      if(valor.toInt()==0){
      digitalWrite (In1,LOW);
      digitalWrite (In2,LOW);
      analogWrite (EnA,0);
      result = "detenido";
    }
      else if(valor.toInt()>0){
      digitalWrite (In1,HIGH);
      digitalWrite (In2,LOW);
      analogWrite (EnA,valor.toInt());
      result = "adelante";
    }
    else if(valor.toInt()<0){
      digitalWrite (In2,HIGH);  
      digitalWrite (In1,LOW);
      y= -(valor.toInt());
      analogWrite (EnA,y);
      
      result = "reversa";
      
    } 
    
      Serial.print("Move....: ");
      Serial.println(valor);

    
  }
      
  /** else if(llave == "z"){
      foto=analogRead(ldr);
      if(foto){
        result = "es de día";}
      }
      */
   
 
  else if(llave == "dir"){
    if(valor.toInt() == -1){
      digitalWrite (In3,HIGH);
      digitalWrite (In4,LOW);
      analogWrite(EnB,1000);
      result = "izquierda";
      Serial.println("Girando izquierda");
      }

      else if(valor.toInt() == 0){
      digitalWrite (In3,LOW);
      digitalWrite (In4,LOW);
      analogWrite(EnB,0);
      result = "directo";
      Serial.println("directo");
      }

      else if(valor.toInt() == 1){
      digitalWrite (In3,LOW);
      digitalWrite (In4,HIGH);
      analogWrite(EnB,1000);
      result = "derecha";
      Serial.println("Girando derecha");
      }
   
  }
  else if(llave[0] == 'l'){
    Serial.println("Cambiando Luces");
    Serial.print("valor luz: ");
    Serial.println(valor);
    //Recomendación utilizar operadores lógico de bit a bit (bitwise operators)
    switch (llave[1]){
            case 'f':
      //# AGREGAR CÓDIGO PARA ENCENDER LUCES FRONTALES
      if(valor=="1"){
        fr = 1;
        data = data & 0b10111101;
        result = "Luces Frontales encendidas";
        Serial.println("Luces frontales");
      }
       else if(valor=="0"){
        if(Diz==1 || Dde==1 || tra==1){
        fr = 0;
        data = data ^ 0b10111101;
        data = data ^ 0b11111111;
        result = "Luces Frontales Apagadas";
        Serial.println("Luces frontales");
         }
         else{
         fr = 0;
         data = data | 0b11111111;
         result = "Luces Frontales Apagadas";
         Serial.println("Luces frontales");
          }
        
      }
      
        break;
      case 'b':
      //# AGREGAR CÓDIGO PARA ENCENDER O APAGAR LUCES TRASERAS
      if(valor=="1"){
        tra = 1;
        data = data & 0b11001111;
        result = "Luces Traseras encendidas";
        Serial.println("Luces traseras");
      }
       else if(valor=="0"){
        if(Diz==1 || Dde==1 || fr==1){
        tra = 0;
        data = data ^ 0b11001111;
        data = data ^ 0b11111111;
        result = "Luces Traseras Apagadas";
        Serial.println("Luces traseras");
         }
         else{
         tra = 0;
         data= data | 0b11111111;
         result = "Luces Traseras Apagadas";
         Serial.println("Luces traseras");
          }
       }
        break;
      case 'l':
      //# AGREGAR CÓDIGO PARA ENCENDER O APAGAR DIRECCIONAL IZQUIERDA
       if(valor=="1"){
        Diz = 1;
        data = data & 0b11110111;
        result = "Direccional izq encendidas";
        Serial.println("Luces izquierda");
      }
       else if(valor=="0"){
        if(Dde==1 || fr==1 || tra==1){
          Diz = 0;
          data = data ^ 0b11110111;
          data = data ^ 0b11111111; 
          result = "Direccional izq Apagadas";  
          Serial.println("Luces frontales");       
          }
        else{
        Diz = 0;
        data= data | 0b11111111;
        result = "Direccional izq Apagadas";
        Serial.println("Luces izquierda");
       }
       }
        
        break;
      case 'r':
      //# AGREGAR PARA CÓDIGO PARA ENCENDER O APAGAR DIRECCIONAL DERECHA
       if(valor=="1"){
        Dde = 1;
        data = data & 0b11111011;
        result = "Direccional derecha encendida";
        Serial.println("Luces derechas");
       }
       else if(valor=="0"){
        if(Diz==1 || fr==1 || tra==1){
        Dde = 0;
        data = data ^ 0b11111011;
        data = data ^ 0b11111111;
        result = "Luces Frontales Apagadas";
        Serial.println("Luces frontales");
         }
       
         else{
         Dde = 0;
         data= data | 0b11111111;
         result = "Luces Frontales Apagadas";
         Serial.println("Luces frontales");
          }
        
      }
        break;

      
      /**
       * # AGREGAR CASOS CON EL FORMATO l[caracter]:valor;
       * SI SE DESEAN manejar otras salidas del registro de corrimiento
       */
      default:
        Serial.println("Ninguna de las anteriores");
        
        break;
    }
    //data VARIABLE QUE DEFINE CUALES LUCES SE ENCIENDEN Y CUALES SE APAGAN
    shiftOut(ab, clk, LSBFIRST, data);
  }
  /**
   * El comando tiene el formato correcto pero no tiene sentido para el servidor
   */
  else{
    result = "Undefined key value: " + llave+";";
    Serial.println(result);
  }
  return result;
}

/**
 * Función para obtener los valores de telemetría del auto
 */

String getBate(){
  int batteryLvl = 0;
  int resto = 0;
  vv = analogRead(bat);
  analogV = (3.3/1023)*vv;
  resuB = (100/3.3)*analogV;
  batteryLvl = resuB;
  resto = resuB+5;
  char Bate [16];
  sprintf(Bate, "blvl:%d-%d;", batteryLvl, resto);
  Serial.print("Sensing: ");
  Serial.println(Bate);
  return Bate;
  }

  
String getSense(){
  int light = 0;
  foto= analogRead(ldr);
  if(foto>0){
    light = 1;
    }
  else {
    light = 0;
    }
  
      
  //# EDITAR CÓDIGO PARA LEER LOS VALORES DESEADOS
  
  // EQUIVALENTE A UTILIZAR STR.FORMAT EN PYTHON, %d -> valor decimal
  char sense [16];
  sprintf(sense, "ldr:%d;", foto);
  Serial.print("Sensing: ");
  Serial.println(sense);
  return sense;
}
