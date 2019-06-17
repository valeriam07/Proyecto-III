from tkinter import *

from tkinter import ttk

from tkinter import font

import os

from threading import Thread        

import threading                     

import os                           

import time                         

from tkinter import messagebox      

import tkinter.scrolledtext as tkscrolled

##### Biblioteca para el Carro

from WiFiClient import NodeMCU

from pruebatabla import *

myCar = NodeMCU()

myCar.start()

msjRec=""

msjEnv=""




colorfondo= "#CC99FF"
textomorado= "#333399"
textoazul= "#0066FF"
textonaranja="#FF5500"
fondo2= "#99CCFF"
fondo3="#40E0D0"
fondo4="#FFCC99"
fondo5="#AFEEEE"


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


#-----------------Movimientos-----------------------------
    
def Up():
    print("Avanza")
    return enviar("pwm:1000;")

def Down():
    print("Retrocede")
    return enviar("pwm:-1000;")

def Left():
    print("Izquierda")
    enviar("dir:-1;")

def Right():
    print("Derecha")
    enviar("dir:1;")

def Stop():
    print("Detenido")
    enviar("det;")


#------------------------Ventanas-------------------------------------
    
def About():
    print ("Ventana de About")
    return Vabout()

def TablaPos():
    print("Tabla de posiciones")
    return Vtablapos()

def TestDrive():
    print("Test Drive")
    return Vtest()

def Edit():
    print("Edit")
    return Vedit()

def pilotos():
    ventana  = tk.Tk()
    ventana_reporte(parent=ventana)
    ventana.mainloop()
    print("pilotos")

def carros():
    print("carros")

def logos():
    print("logos")

def patrocinadores():
    print("patrocinadores")

def Menú():
    #v.iconify()
    v_inicio.deiconify()
    #v_tabla.iconify()
    print("iconify")

#-------------------------Escuderias--------------------------

def Kerosene():
    print("Kerosene")
    return Vkerosene()

def Fiji():
    print("Fiji")
    return Vfiji()

ESC="Kerosene"

def select_escuderia():
    global ESC
    ESC=SpinB_escuderia.get()
    print("escuderia seleccionada:",ESC)


#-------------------------Ventana Principal--------------------
    
v_inicio= Tk()
v_inicio.title("Formula-E")
v_inicio.geometry("700x600")
v_inicio.configure(background=colorfondo)

C_escuderia=Text(v_inicio,width=40,height=26)

Lb_escuderias=Label(v_inicio,text="Escuderías",font=("Cambria",17),fg=textomorado,background=colorfondo).place(x=50,y=60)

Lb_escuderias=Label(v_inicio,text="Información",font=("Cambria",15),fg=textomorado).place(x=55,y=115)

Bt_Kerosene=Button(v_inicio,text="Kerosene",command=Kerosene,bg=fondo2,width=15,height=2).place(x=70,y=170)

Bt_E2=Button(v_inicio,text="Fiji Republic",command=Fiji,bg=fondo2,width=15,height=2).place(x=70,y=250)


C_escuderia.place(x=40,y=100)


Lb_Tinicio=Label(v_inicio,text="Formula-E Inicio",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=280,y=5)


Lb_temporada=Label(v_inicio,text="Temporada",font=("Cambria",12),background=colorfondo).place(x=400,y=50)

Lb_estadoactual=Label(v_inicio,text="Estado del auto en la temporada actual",font=("Cambria",12),background=colorfondo).place(x=400,y=200)

Lb_indiceganador=Label(v_inicio,text="Índice Ganador de Escudería",font=("Cambria",12),background=colorfondo).place(x=400,y=400)

Bt_About=Button(v_inicio,text="About",command=About,bg=fondo2).place(x=50,y=550)

Bt_TablaPos=Button(v_inicio,text="Tabla de posiciones",command=TablaPos,bg=fondo2).place(x=110,y=550)

Bt_TestDrive=Button(v_inicio,text="Test Drive",command=TestDrive,bg=fondo2).place(x=240,y=550)

Bt_Editar=Button(v_inicio,text="Editar",command=Edit).place(x=60,y=480)

Lb_escuderias=Label(v_inicio,text="Seleccione una escudería").place(x=55,y=350)

SpinB_escuderia=ttk.Combobox(v_inicio,values=("Kerosene","Fiji Republic"))
SpinB_escuderia.current(0)
SpinB_escuderia.place(x=70,y=400)

Bt_Editar=Button(v_inicio,text="Listo",command= select_escuderia).place(x=250,y=397)



#--------------------------Cambios en los Patrocinadores----------------------------------

PAT=PhotoImage(file="RedBull.png")
PATF=PhotoImage(file="Gucci.png")

def PatChanges(PatK):
    
    if(PatK=="Red Bull"):
        imagen=PhotoImage(file="RedBull.png")
        return imagen
    elif(PatK=="Cheetos"):
        imagen=PhotoImage(file="cheetos.png")
        return imagen
    elif(PatK=="Gucci"):
        imagen=PhotoImage(file="Gucci.png")
        return imagen
    elif(PatK=="Fila"):
        imagen=PhotoImage(file="Fila.png")
        return imagen
    else:
        ''
def PatChanges2(PatF,v_edit):
    v_inicio.deiconify()
    v_edit.iconify()
    print(PatF)
    if(PatF=="Red Bull"):
        imagen2=PhotoImage(file="RedBull.png")
        return imagen2
    elif(PatF=="Cheetos"):
        imagen2=PhotoImage(file="cheetos.png")
        return imagen2
    elif(PatF=="Gucci"):
        imagen2=PhotoImage(file="Gucci.png")
        return imagen2
    elif(PatF=="Fila"):
        imagen2=PhotoImage(file="Fila.png")
        return imagen2
    else:
        ''

#----------------------------Cambios en los Logos--------------------------

        
LOGOK=PhotoImage(file="logo2_K.png")
LOGOF=PhotoImage(file="logo2_F.gif")

def logo1(LogoK):
    print("You selected:",LogoK)
    if(LogoK=="Logo 1"):
        imagen=PhotoImage(file="logo2_K.png")
        return imagen
    elif(LogoK=="Logo 2"):
        imagen=PhotoImage(file="logo3_K.png")
        return imagen
    else:
        ''
        

def logo2(LogoF,v_edit):
    v_inicio.deiconify()
    v_edit.iconify()
    print("You selected:",LogoF)
    if(LogoF=="Logo 1"):
        imagen=PhotoImage(file="logo2_F.gif")
        return imagen
    elif(LogoF=="Logo 2"):
        imagen=PhotoImage(file="logo3_F.png")
        return imagen
    else:
        ''

#-------------------------Variables de Pilotos y Carros-----------------------------

PILOTOK="Florentino"
PILOTOF="PineBerry"
CARROK="Tesla"
CARROF="VolksWagen"

PILOTO_TD=""
CARRO_TD=""
NAC=""


def PyC():
    global ESC
    global PILOTO_TD
    global CARRO_TD
    global NAC
    
    if (ESC=="Kerosene"):
        PILOTO_TD=PILOTOK
        CARRO_TD=CARROK
        NAC= "Italia"
        
        
    elif(ESC=="Fiji Republic"):
        PILOTO_TD=PILOTOF
        CARRO_TD=CARROF
        NAC= "Fiji"

    else:
        ''
        
        
    
#----------------------------------Escuderia 1------------------------------------       
def Vkerosene():
    
    def ReadyK():
        global PILOTOK
        PilotK=SpinB_pilotos.get()
        PILOTOK= PilotK
        print("Kerosene pilot:",PILOTOK)

        global CARROK
        CarK=SpinB_carros.get()
        CARROK= CarK
        print("Kerosene Car:",CARROK)

        v_esc1.iconify()
        v_inicio.deiconify()


    v_esc1=Toplevel()
    v_esc1.title("Formula-E")
    v_esc1.geometry("700x600")
    v_esc1.configure(background=colorfondo)

    Lb_escuderia=Label(v_esc1,text="Información de la Escudería",font=("Cambria",18),background=colorfondo).place(x=200,y=50)

    C_escuderia=Text(v_esc1,width=40,height=27)

    C_escuderia.insert(INSERT,"Nombre: Kerosene"+'\n'+'\n'+'\n''\n'+"Ubicación Geográfica: Italia"+'\n'+'\n'+'\n''\n'+"Pilotos Disponibles: Florentino, Smyrno, Francesca"+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+"Automoviles Registrados: Tesla, Ferrari, McLaren")

    SpinB_pilotos=ttk.Combobox(v_esc1,values=("Florentino","Smyrno","Francesca"))
    SpinB_pilotos.current(0)
    SpinB_pilotos.place(x=100,y=300)

    SpinB_carros=ttk.Combobox(v_esc1,values=("Tesla","Ferrari","McLaren"))
    SpinB_carros.current(0)
    SpinB_carros.place(x=100,y=425)

    C_escuderia.place(x=80,y=100)

    Lb_logo=Label(v_esc1,text="Logo",font=("Cambria",15),background=colorfondo).place(x=500,y=350)
    
    Lb_logoimg=Label(v_esc1,image=LOGOK).place(x=500,y=400)

    Lb_Patrocinadores=Label(v_esc1,text="Patrocinador",font=("Cambria",15),background=colorfondo).place(x=500,y=125)

    Lb_ImgPat=Label(v_esc1,image=PAT).place(x=500,y=175)

    Bt_Ready=Button(v_esc1,text="Listo",command=ReadyK,width=10,bg=fondo2).place(x=80,y=550)
    
    v_esc1.mainloop()

#----------------------------------Escuderia 2-----------------------------

def Vfiji():

    def ReadyF():
        global PILOTOF
        PilotF=SpinB_pilotos.get()
        PILOTOF= PilotF
        print("Fiji Republic pilot:",PILOTOF)

        global CARROF
        CarF=SpinB_carros.get()
        CARROF= CarF
        print("Fiji Republic car:",CARROF)

        v_esc2.iconify()
        v_inicio.deiconify()
        


    v_esc2=Toplevel()
    v_esc2.title("Formula-E")
    v_esc2.geometry("700x600")
    v_esc2.configure(background=colorfondo)

    Lb_escuderia=Label(v_esc2,text="Información de la Escudería",font=("Cambria",18),background=colorfondo).place(x=200,y=50)

    C_escuderia=Text(v_esc2,width=40,height=27)

    C_escuderia.insert(INSERT,"Nombre: Fiji Republic"+'\n'+'\n'+'\n''\n'+"Ubicación Geográfica: Melanesia"+'\n'+'\n'+'\n''\n'+"Pilotos Disponibles: Nil, Alaiah, PineBerry"+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+'\n'+"Automoviles Registrados: Porsche, VolksWagen, Maserati")

    SpinB_pilotos=ttk.Combobox(v_esc2,values=("Nil","Alaiah","PineBerry"))
    SpinB_pilotos.current(0)
    SpinB_pilotos.place(x=100,y=300)

    SpinB_carros=ttk.Combobox(v_esc2,values=("Porsche","VolksWagen","Maserati"))
    SpinB_carros.current(0)
    SpinB_carros.place(x=100,y=425)

    C_escuderia.place(x=80,y=100)

    Lb_logo=Label(v_esc2,text="Logo",font=("Cambria",15),background=colorfondo).place(x=500,y=350)
    
    Lb_logoimg=Label(v_esc2,image=LOGOF).place(x=500,y=400)    

    Lb_Patrocinadores=Label(v_esc2,text="Patrocinadores",font=("Cambria",15),background=colorfondo).place(x=500,y=125)

    Lb_ImgPat=Label(v_esc2,image=PATF).place(x=500,y=175)

    Bt_Ready=Button(v_esc2,text="Listo",command=ReadyF,width=10,bg=fondo2).place(x=80,y=550)
    
    v_esc2.mainloop()

#---------------------Ventana About---------------------

def Vabout():
    v_inicio.iconify()
    
    v_about=Tk()
    v_about.title("Formula-E")
    v_about.geometry("700x600")
    v_about.configure(background=colorfondo)

    Lb_Tabout=Label(v_about,text="Ventana de About",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=260,y=5)

    C_creditos=Text(v_about,width=50,height=30)
    C_creditos.insert(INSERT,"Institución: \t Instituto Tecnológico de Costa Rica"+'\n'+'\n'+"Autoras:"+'\n'+"\t Estefanny Villalta \t carne"+'\n'+"\t Valeria Morales \t 2019052012"+
    '\n'+'\n'+"Carrera: \t Ingeniería en Computadores"+'\n'+'\n'+"Curso: \t Taller de Programación"+'\n'+'\n'+"Grupo: \t #03"+'\n'+'\n'+"Año: \t 2019"+
    '\n'+'\n'+"Profesor: \t Pedro Gutiérrez"+'\n'+'\n'+"País de Producción: \t Costa Rica"+'\n'+'\n'+"Versión del Programa: \t Python 3.7")
    
    C_creditos.place(x=150,y=50)
    Bt_Menu=Button(v_about,text="Volver al Menú",command=Menú().place(x=40,y=550))
    v_about.mainloop()

    
    
#------------------------Tabla de Posiciones-------------------------
def RKpilotos():
    v_inicio.iconify()
    editar_info()
    '''
    print("RK pilotos")
    #v_tabla.destroy()
    v_inicio.iconify()
    

    v_RKpilotos=Tk()
    v_RKpilotos.title("Formula-E")
    v_RKpilotos.geometry('700x600')
    v_RKpilotos.configure(background=colorfondo)
    
    Lb_Tpilotos=Label(v_RKpilotos,text="Ranking de Pilotos",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=260,y=5)

    v_RKpilotos.mainloop()
    '''
    
def RKautos():
    print("RK autos")
    v_inicio.iconify()
    v_RKautos=Tk()
    v_RKautos.title("Formula-E")
    v_RKautos.geometry('700x600')
    v_RKautos.configure(background=colorfondo)
    
    Lb_Tautos=Label(v_RKautos,text="Ranking de Automóviles",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=240,y=5)

    v_RKautos.mainloop()
    
def Vtablapos():
    v_inicio.iconify()
    def cerrar1():
        v_tabla.iconify()
        RKpilotos()

    def cerrar2():
        v_tabla.iconify()
        RKautos()
    
    v_tabla=Tk()
    v_tabla.title("Formula-E")
    v_tabla.geometry("400x300")
    v_tabla.configure(background=colorfondo)

    Lb_Ttabla=Label(v_tabla,text="Tabla de Posiciones",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=100,y=5)

    
    Bt_pilotos= Button(v_tabla,text="Ranking de Pilotos",font=("News Gothic",15),bg=fondo2,width=20,height=3,anchor="center",command=cerrar1).place(x=80,y=60)
    Bt_autos= Button(v_tabla,text="Ranking de Automóviles",font=("News Gothic",15),bg=fondo2,width=20,height=3,anchor="center",command=cerrar2).place(x=80,y=165)

    Bt_Menu=Button(v_tabla,text="Volver al Menú",command=Menú).place(x=40,y=250)
    v_tabla.mainloop()
    
#---------------------------Editar-----------------------------
    
patrocinador=StringVar()

def Vedit():

    
    def Pat():
        global PAT
        global PATF
        global LOGOF
        global LOGOK

        PatK= Cbox_kerosene.get()
        PatF= Cbox_Fiji.get()
        PAT= PatChanges(PatK)
        PATF= PatChanges2(PatF,v_edit)

        LogoK= SpinB_logosK.get()
        LogoF= SpinB_logosF.get()
        LOGOK= logo1(LogoK)
        LOGOF= logo2(LogoF)
        
    
        
          
    v_inicio.iconify()
    
    v_edit=Toplevel()
    v_edit.title("Formula-E")
    v_edit.geometry("1000x1000")
    v_edit.configure(background=colorfondo)

    Lb_Teditar=Label(v_edit,text="Editar Informacion",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=260,y=5)

    Lb_logosK=Label(v_edit,text="Seleccione un Logo para Fiji Republic",background=colorfondo).place(x=500,y=100)
    
    Lb_logosF=Label(v_edit,text="Seleccione un Logo para Kerosene",background=colorfondo).place(x=750,y=100)
    
    SpinB_logosK= ttk.Combobox(v_edit,values=("Logo 1","Logo 2"))
    SpinB_logosK.current(0)
    SpinB_logosK.place(x=500,y=120)

    SpinB_logosF= ttk.Combobox(v_edit,values=("Logo 1","Logo 2"))
    SpinB_logosF.current(0)
    SpinB_logosF.place(x=750,y=120)

    Lb_patrocinador=Label(v_edit,text="Seleccione un patrocinador de temporada",background=colorfondo).place(x=50,y=70)

    Lb_patrocinador1=Label(v_edit,text="Para Kerosene:",background=colorfondo).place(x=70,y=100)

    Cbox_kerosene=ttk.Combobox(v_edit,values=("Red Bull","Cheetos","Gucci","Fila"))
    Cbox_kerosene.current(0)
    Cbox_kerosene.place(x=70,y=120)

    Lb_patrocinador2=Label(v_edit,text="Para Fiji Republica:",background=colorfondo).place(x=300,y=100)

    Cbox_Fiji=ttk.Combobox(v_edit,values=("Red Bull","Cheetos","Gucci","Fila"))
    Cbox_Fiji.current(0)
    Cbox_Fiji.place(x=300,y=120)

    Img1= PhotoImage(file="RedBull.png")
    Lb_P1= Label(v_edit,image=Img1).place(x=50,y=200)

    Img2=PhotoImage(file="cheetos.png")
    Lb_P2= Label(v_edit,image=Img2).place(x=50,y=400)

    Img3=PhotoImage(file="Gucci.png")
    Lb_P3= Label(v_edit,image=Img3).place(x=260,y=200)

    Img4=PhotoImage(file="Fila.png")
    Lb_P4= Label(v_edit,image=Img4).place(x=260,y=400)

    Logo1F=PhotoImage(file="logo2_F.gif")
    Lb_L1F= Label(v_edit,image=Logo1F).place(x=500,y=200)

    Logo2F=PhotoImage(file="logo3_F.png")
    Lb_L2F= Label(v_edit,image=Logo2F).place(x=520,y=370)

    Logo1K=PhotoImage(file="logo2_K.png")
    Lb_L1K= Label(v_edit,image=Logo1K).place(x=750,y=200)

    Logo2K=PhotoImage(file="logo3_K.png")
    Lb_L2K= Label(v_edit,image=Logo2K).place(x=750,y=400)

    Lb_Logo_K1=Label(v_edit,text="Logo 1",background=colorfondo).place(x=500,y=175)

    Lb_Logo_K2=Label(v_edit,text="Logo 2",background=colorfondo).place(x=490,y=350)

    Lb_logo_F1=Label(v_edit,text="Logo 1",background=colorfondo).place(x=750,y=175)

    Lb_logo_F2=Label(v_edit,text="Logo 2",background=colorfondo).place(x=750,y=370)
    
    Bt_Save=Button(v_edit,text="Guardar Cambios",command=Pat).place(x=800,y=600)
    
    Bt_Menu=Button(v_edit,text="Volver al Menú",command=Menú).place(x=600,y=600)


        
    v_edit.mainloop()


#---------------------------Test Drive-----------------------------------

    
def Vtest():
    
    v_inicio.iconify()

    v_test=Toplevel()
    v_test.title("Formula-E")
    v_test.geometry("1000x600")

    carview= PhotoImage(file="Carro1.png")
    Lb_background= Label(v_test,image=carview,width=1000,height=600).place(x=0,y=0)

    Bt_avanza=Button(v_test,text='Avanzar',font=("Impact",20),fg=textonaranja,bg=fondo3,width=10,height=1,anchor="center",command= Up).place(x=475,y=50)

    Bt_retroceso=Button(v_test,text='Retroceder',font=("Impact",20),fg=textonaranja,bg=fondo3,width=10,height=1,anchor="center",command= Down).place(x=475,y=200)
                                                              
    Bt_izquierda=Button(v_test,text='Izquierda',font=("Impact",20),fg=textonaranja,bg=fondo3,width=10,height=1,anchor="center",command= Left).place(x=335,y=125)

    Bt_derecha= Button(v_test,text='Derecha',font=("Impact",20),fg=textonaranja,bg=fondo3,width=10,height=1,anchor="center", command= Right).place(x=610,y=125)
    
    Bt_stop= Button(v_test,text= 'Stop',font=("Impact",20),fg=fondo3,bg=textonaranja,anchor="center", command= Stop).place(x=505,y=120)

    Lb_pwm=Label(v_test,text="PWM",width=20,height=3).place(x=425,y=475)

    PyC()

    Lb_name=Label(v_test,text=PILOTO_TD,width=15,height=2,bg=fondo4,font=("News Gothic",12)).place(x=825,y=20)
    Lb_car=Label(v_test,text=CARRO_TD,width=15,height=2,bg=fondo4,font=("News Gothic",12)).place(x=825,y=75)
    
    Lb_nac=Label(v_test,text=NAC,width=15,height=2,bg=fondo4,font=("News Gothic",12)).place(x=825,y=125)

    Lb_escuderia=Label(v_test,text=ESC,width=15,height=3,bg=fondo5,font=("News Gothic",12)).place(x=30,y=200)

    blvl= PhotoImage(file="bateria.png")
    Lb_bateria= Label(v_test,image=blvl,width=55,height=130).place(x=20,y=20)
    

    #foto= PhotoImage(file="")
    #Lb_fotocelda= Label(v_test,image=foto,width=100,height=100).place(x=10,y=10)
    

    v_test.mainloop()

#font=("News Gothic",15),width=20,height=3,anchor="center",command=RKpilotos).place(x=80,y=60)



#FALTA HACER QUE LAS VENTANAS SE DESTRUYAN 


v_inicio.mainloop()
