from tkinter import *
#import tkinter as tk
from tkinter import font
import os






colorfondo= "#CC99FF"
textomorado= "#333399"
textoazul= "#0066FF"
fondo2= "#99CCFF"


#Ventana de inicio
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
    
v_inicio= Tk()
v_inicio.title("Formula-E")
v_inicio.geometry("700x600")
v_inicio.configure(background=colorfondo)

Lb_Tinicio=Label(v_inicio,text="Formula-E Inicio",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=280,y=5)

Lb_escuderia=Label(v_inicio,text="Información de la Escudería",font=("Cambria",15),background=colorfondo).place(x=50,y=50)


C_escuderia=Text(v_inicio,width=40,height=27)

C_escuderia.insert(INSERT,"Nombre: Kerosene"+'\n'+'\n'+'\n'+"Logo:"+'\n'+'\n'+'\n'+'\n'+'\n'+"Ubicación Geográfica: Italia"+'\n'+'\n'+'\n'+"Patrocinadores:"+'\n'+'\n'+'\n'+'\n'+"Pilotos Disponibles:"+'\n'+'\n'+'\n'+'\n'+"Automoviles Registrados:")

SpinB_pilotos=Spinbox(values=("Name1","Name2","Name3","Name4","Name5","Name6","Name7","Name8","Name9","Name10"),command=pilotos).place(x=60,y=350)

SpinB_carros=Spinbox(values=("Carro1","Carro2","Carro3","Carro4","Carro5"),command=carros).place(x=60,y=415)

C_escuderia.place(x=50,y=80)


#Falta mecanismo para editar el logo y los patrocinadores

Lb_temporada=Label(v_inicio,text="Temporada",font=("Cambria",12),background=colorfondo).place(x=400,y=50)

Lb_estadoactual=Label(v_inicio,text="Estado del auto en la temporada actual",font=("Cambria",12),background=colorfondo).place(x=400,y=200)

Lb_indiceganador=Label(v_inicio,text="Índice Ganador de Escudería",font=("Cambria",12),background=colorfondo).place(x=400,y=400)

Bt_About=Button(v_inicio,text="About",command=About,bg=fondo2).place(x=50,y=550)

Bt_TablaPos=Button(v_inicio,text="Tabla de posiciones",command=TablaPos,bg=fondo2).place(x=110,y=550)

Bt_TestDrive=Button(v_inicio,text="Test Drive",command=TestDrive,bg=fondo2).place(x=240,y=550)

Bt_Editar=Button(v_inicio,text="Editar",command=Edit).place(x=60,y=480)

#Ventana de about

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
    Bt_Menu=Button(v_about,text="Volver al Menú",command=Menú).place(x=40,y=550)
    
#Ventana de Tabla de Posiciones
def RKpilotos():
    print("RK pilotos")
    #v_tabla.destroy()
    v_inicio.iconify()
    

    v_RKpilotos=Tk()
    v_RKpilotos.title("Formula-E")
    v_RKpilotos.geometry('700x600')
    v_RKpilotos.configure(background=colorfondo)
    
    Lb_Tpilotos=Label(v_RKpilotos,text="Ranking de Pilotos",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=260,y=5)


def RKautos():
    print("RK autos")
    v_inicio.iconify()
    v_RKautos=Tk()
    v_RKautos.title("Formula-E")
    v_RKautos.geometry('700x600')
    v_RKautos.configure(background=colorfondo)
    
    Lb_Tautos=Label(v_RKautos,text="Ranking de Automóviles",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=240,y=5)
    
def Vtablapos():
    #v_inicio.iconify()
    
    v_tabla=Tk()
    v_tabla.title("Formula-E")
    v_tabla.geometry("400x300")
    v_tabla.configure(background=colorfondo)

    Lb_Ttabla=Label(v_tabla,text="Tabla de Posiciones",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=100,y=5)

    
    Bt_pilotos= Button(v_tabla,text="Ranking de Pilotos",font=("News Gothic",15),bg=fondo2,width=20,height=3,anchor="center",command=RKpilotos).place(x=80,y=60)
    Bt_autos= Button(v_tabla,text="Ranking de Automóviles",font=("News Gothic",15),bg=fondo2,width=20,height=3,anchor="center",command=RKautos).place(x=80,y=165)

    Bt_Menu=Button(v_tabla,text="Volver al Menú",command=Menú).place(x=40,y=250)
    v_tabla.mainloop()
#Ventana para editar info
    
patrocinador=StringVar()

def Vedit():
    v_inicio.iconify()
    
    v_edit=Toplevel()
    v_edit.title("Formula-E")
    v_edit.geometry("700x600")
    v_edit.configure(background=colorfondo)

    Lb_Teditar=Label(v_edit,text="Editar Informacion",font=("Cambria",18),fg=textomorado,background=colorfondo).place(x=260,y=5)

    Lb_logos=Label(v_edit,text="Seleccione un Logo",background=colorfondo).place(x=50,y=70)

    
    SpinB_logos=Spinbox(values=("Logo 1","Logo 2","Logo 3"),command=logos).place(x=50,y=100)

    Lb_patrocinador=Label(v_edit,text="Inserte el nombre del patrocinador/es de temporada",background=colorfondo).place(x=50,y=170)

    Img1= PhotoImage(file="RedBull.png")
    Lb_P1= Label(v_edit,image=Img1).place(x=50,y=200)
    
    SpinB_patr=Spinbox(values=("Patrocinador 1","Patrocinador 2","Patrocinador 3"),command=patrocinadores).place(x=50,y=100)
    
    Bt_Menu=Button(v_edit,text="Volver al Menú",command=Menú).place(x=40,y=550)
    v_edit.mainloop()

def Vtest():
    
    v_inicio.iconify()

    v_test=Toplevel()
    v_test.title("Formula-E")
    v_test.geometry("1280x720")

    carview= PhotoImage(file="Carro1.png")
    Lb_background= Label(v_test,image=carview).place(x=10,y=10)
    Vtest.mainloop()
    

    #Seleccione un logo
    #poner logos por numero
    #inserte el patrocinador


#FALTA HACER QUE LAS VENTANAS SE DESTRUYAN 


v_inicio.mainloop()
