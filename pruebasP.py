
#leer mensajes de ideArduino al programa en python
#arduino.readline() es la funcion que lee lo que sucede en el lenguaje arduino
#por medio de el serial.println(valor) en el programa de arduino

"""import serial, time
arduino = serial.Serial('COM4', 9600)
time.sleep(2)
rawString = arduino.readline()
print(rawString)
arduino.close()"""

from tkinter import *               
from threading import Thread        
import threading                     
import os                           
import time                         
from tkinter import messagebox      
import tkinter.scrolledtext as tkscrolled
##### Biblioteca para el Carro
from WiFiClient import NodeMCU


"""llamada a la clase NodeMCU"""
myCar = NodeMCU()
myCar.start()


"""variables globales que guardan
los valores recividos y enviados"""
msjRec=""
msjEnv=""

#Es importante que está función siga corriendo
#ya que es la que actualiza los mensajes de entrada del NodeMCU
#Además de los de salida (por eso hay un retorno de la función enviar a esta)


def obIn():
    indice=0
    while(myCar.loop):
        while(indice < len(myCar.log)):
            global msjRec
            global msjEnv
            """myCar.Log[indice] es el mensaje de respuesta([0]) o
                de envío de msj ([1]), estos valores son consecuentes
                respecto al comando, así que respecto a estas variables
                se harán las acciones de los eventos(comandos)
                """
            msjRec = myCar.log[indice][0]
            msjEnv = myCar.log[indice][1]

        
            print(msjRec,msjEnv)
            indice+=1
        time.sleep(0.200)
    p = Thread(target=get_log)
    p.start()

         
def enviar(x):
    """x está funcionando como comandos (cambiar por eventos en la interfaz)
    ya sea botones o teclas que equivalgan a los comandos"""
    if(isinstance(x,str)):
        myCar.send(x)
        """este return no es necesario a la hora de hacer la parte
        gráfica se soluciona con el main loop de tkinter"""
        return obIn()
    else:
        return False


#Probar llamando a enviar con x siendo algún comando
#previamente programado en el NodeMCU


        
        
    
