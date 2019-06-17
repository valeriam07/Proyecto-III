import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import *

#-------------------------Variables Globales------------------

fondo2= "#99CCFF"
textomorado= "#333399"

PILOT=''
ORD=''




datos=[[10,10,"Florentino",25,"Italia","Kerosene"],
       [9,9,"Smyrno",30,"Italia","Kerosene"],
       [8,8,"Francesca",27,"Italia","Kerosene"],
       [7,7,"Nil",31,"Fiji","Fiji Republic"],
       [6,6,"Alaiah",22,"Fiji","Fiji Republic"],
       [5,5,"PineBerry",28,"Fiji","Fiji Republic"]]


carros=[[10,"Tesla","model 3",0,"Kerosene","\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",''],
        [9,"Ferrari",488,0,"Kerosene",'',''],
        [8,"McLaren",720,0,"Kerosene",'',''],
        [7,"Porshe",918,0,"Fiji Republic",'',''],
        [6,"VolksWagen","Arteon",0,"Fiji Republic",'',''],
        [5,"Maserati","Luxury Sedan",0,"Fiji Republic",'','']]
       



#-------------------------Tabla Pilotos-------------------------------------------    

class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#40E0D0",font=("Helvetica", 16))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")
        



        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)



def ventana_reporte(parent=None):
    global datos,ORD
    t3 = tk.Toplevel(parent, bg="#E8C8CD")
    t3.title("Formula-E")
    t3.geometry('700x600')
    t3.configure(bg="#CC99FF")
    
    Img3=PhotoImage(file="fondo2img.png")
    Lb_P3= Label(t3,image=Img3).place(x=-50,y=0)

    
    
    t3.focus_set()
    t3.grab_set()
    #Lb_ord=Label(t3,text=("La tabla esta ordenada según el:",ORD),font=("News Gothic",12),background="#CC99FF").place(x=100,y=50)

    pilotos_headers = (u"Posición", u"REP",   u"RGP", u"Nombre",
                        u"Edad", u"Nacionalidad",   u"Escuderia"
                        )


    pilotos_tab = Table(t3, title="Ranking de Pilotos", headers=pilotos_headers,width=70,height=15)
    pilotos_tab.place(x=100,y=100)

    cursor = ((u"1",datos[0][0], datos[0][1], datos[0][2], datos[0][3], datos[0][4], datos[0][5]),
              (u"2",datos[1][0], datos[1][1], datos[1][2], datos[1][3], datos[1][4], datos[1][5]),
              (u"3",datos[2][0], datos[2][1], datos[2][2], datos[2][3], datos[2][4], datos[2][5]),
              (u"4",datos[3][0], datos[3][1], datos[3][2], datos[3][3], datos[3][4], datos[3][5]),
              (u"5",datos[4][0], datos[4][1], datos[4][2], datos[4][3], datos[4][4], datos[4][5]),
              (u"6",datos[5][0], datos[5][1], datos[5][2], datos[5][3], datos[5][4], datos[5][5])
              )

    for row in cursor:
        pilotos_tab.add_row(row)

    t3.mainloop()



def llamar():
    ventana  = tk.Toplevel()
    ventana.geometry('1x1')
    ventana_reporte(parent=ventana)
    ventana.mainloop()

#llamar()


#------------------Ordenamiento-----------------------------------


def ordenar():
    global ORD
    
    if(ORD=="RGP"):
        return ordenar_REP_RGP(0,1)
    
    elif(ORD=="REP"):
        return ordenar_REP(0,0)

    else:
        ''

def ordenar_REP_RGP(i,j):
    global datos

    if(i==len(datos)-1):
       print (datos)
       
    elif(datos[i][j]<datos[i+1][j]):
       value=datos[i]
       datos[i]=datos[i+1]
       datos[i+1]=value
       return ordenar_REP_RGP(0,j)

    else:
       return ordenar_REP_RGP(i+1,j)





#--------------------Editar Info-------------------------------

def REP_RGP(V,T,A,P):
    print("REP")
    V=V.get()
    T=T.get()
    A=A.get()
    P=P.get()
    
    rep=int((V/(T-A))*100)
    print("El REP es:",rep)

    rgp=int(((V+P)/(T-A))*100)
    print("El RGP es:",rgp)

    return asignar_piloto(rep,rgp)

def asignar_piloto(rep,rgp):
    global datos
    
    if(PILOT=="Florentino"):
        datos[0][0]=rep
        datos[0][1]=rgp
        return ordenar()

    elif(PILOT=="Smyrno"):
        datos[1][0]=rep
        datos[1][1]=rgp
        return ordenar()

    elif(PILOT=="Francesca"):
        datos[2][0]=rep
        datos[2][1]=rgp
        return ordenar()

    elif(PILOT=="Nil"):
        datos[3][0]=rep
        datos[3][1]=rgp
        return ordenar()

    elif(PILOT=="Alaiah"):
        datos[4][0]=rep
        datos[4][1]=rgp
        return ordenar()

    elif(PILOT=="PineBerry"):
        datos[5][0]=rep
        datos[5][1]=rgp
        return ordenar()

    else:
        ''

        

def editar_info():

    def select_pilot():
        global PILOT
        PILOT= SpinB_piloto.get()

        global ORD
        ORD= SpinB_cat.get()

        REP_RGP(V,T,A,P)
        
        
        
    v_info=Tk()
    v_info.title("Formula-E")
    v_info.geometry("700x600")
    v_info.configure(background=fondo2)

    V=IntVar()
    A=IntVar()
    T=IntVar()
    P=IntVar()

    Lb_titulo=Label(v_info,text="Editar Información de los Pilotos",font=("Cambria",18),fg=textomorado,background=fondo2).place(x=280,y=5)

    Lb_titulo=Label(v_info,text="Seleccione el piloto en el que desea realizar cambios",font=("News Gothic",12),background=fondo2).place(x=70,y=100)

    SpinB_piloto=ttk.Combobox(v_info,values=("Florentino","Smyrno","Francesca","Nil","Alaiah","PineBerry"))
    
    SpinB_piloto.current(0)
    SpinB_piloto.place(x=70,y=140)


    Lb_V=Label(v_info,text="Cantidad de Victorias:",font=("News Gothic",12),background=fondo2).place(x=70,y=200)

    En_V=Entry(v_info,textvariable=V).place(x=70,y=240)

    Lb_P=Label(v_info,text="Cantidad de 2do y 3er lugar:",font=("News Gothic",12),background=fondo2).place(x=70,y=270)

    En_P=Entry(v_info,textvariable=P).place(x=70,y=300)

    Lb_A=Label(v_info,text="Cantidad de Abandonos:",font=("News Gothic",12),background=fondo2).place(x=300,y=200)

    En_A=Entry(v_info,textvariable=A).place(x=300,y=240)

    Lb_T=Label(v_info,text="Carreras en las que ha participado:",font=("News Gothic",12),background=fondo2).place(x=300,y=270)

    En_T=Entry(v_info,textvariable=T).place(x=300,y=300)

    Bt_Save=Button(v_info,text="Guardar Cambios",command=select_pilot,width=20,height=2).place(x=70,y=500)

    Bt_seguir=Button(v_info,text="Ver Ranking",command=llamar,width=20,height=2).place(x=300,y=500)

    SpinB_cat=ttk.Combobox(v_info,values=("RGP","REP"))
    SpinB_cat.current(0)
    SpinB_cat.place(x=70,y=410)
    Lb_A=Label(v_info,text="Seleccione una Categoría para Ordenar la Tabla:",font=("News Gothic",12),background=fondo2).place(x=70,y=370)

    v_info.mainloop()
    
#editar_info()

#------------------------------Tabla Carros------------------------------------------------

class Cars(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#40E0D0",font=("Helvetica", 16))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")
        



        
    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)



def ventana_reporte(parent=None):
    global datos,ORD
    t3 = tk.Toplevel(parent, bg="#E8C8CD")
    t3.title("Formula-E")
    t3.geometry('950x700')
    t3.configure(bg="#CC99FF")
    
    Img3=PhotoImage(file="fondo2img.png")
    Lb_P3= Label(t3,image=Img3).place(x=0,y=0)
    
    
    
    t3.focus_set()
    t3.grab_set()
    #Lb_ord=Label(t3,text=("La tabla esta ordenada según el:",ORD),font=("News Gothic",12),background="#CC99FF").place(x=100,y=50)

    carros_headers = (u"Posición", u"Eficiencia",   u"Marca", u"Modelo",
                        u"Temporada", u"Escudería",   u"Foto"
                        )


    carros_tab = Table(t3, title="Ranking de Automóviles", headers=carros_headers,width=70,height=25)
    carros_tab.place(x=50,y=40)


    cursor = ((u"1",carros[0][0], carros[0][1], carros[0][2], carros[0][3], carros[0][4], carros[0][5]),("\n"),("\n"),("\n"),
              (u"2",carros[1][0], carros[1][1], carros[1][2], carros[1][3], carros[1][4], carros[1][5]),("\n"),("\n"),("\n"),
              (u"3",carros[2][0], carros[2][1], carros[2][2], carros[2][3], carros[2][4], carros[2][5]),("\n"),("\n"),("\n"),
              (u"4",carros[3][0], carros[3][1], carros[3][2], carros[3][3], carros[3][4], carros[3][5]),("\n"),("\n"),("\n"),
              (u"5",carros[4][0], carros[4][1], carros[4][2], carros[4][3], carros[4][4], carros[4][5]),("\n"),("\n"),("\n"),
              (u"6",carros[5][0], carros[5][1], carros[5][2], carros[5][3], carros[5][4], carros[5][5])
              )

    for row in cursor:
        carros_tab.add_row(row)



    Lb_T= Label(t3,image=carros[0][6]).place(x=700,y=100)

    Lb_F= Label(t3,image=carros[1][6]).place(x=700,y=170)

    Lb_M= Label(t3,image=carros[2][6]).place(x=700,y=250)

    Lb_P= Label(t3,image=carros[3][6]).place(x=700,y=320)

    Lb_V= Label(t3,image=carros[4][6]).place(x=700,y=400)

    Lb_S= Label(t3,image=carros[5][6]).place(x=700,y=480)

    t3.mainloop()





def call():
    ventana  = tk.Toplevel()
    ventana.geometry('0x0')
    ventana_reporte(parent=ventana)
    ventana.mainloop()

#-------------------------Imagen de los Carros----------------------------

'''def select_img(i,j):
    if(i==len(carros-1):
       print("carros asignados")

    elif(carros[i][j]=="Tesla"'''
    


#------------------Ordenar Carros------------------------------------------

def ordenar_ef(i,j):
    global carros

    if(i==len(carros)-1):
       print (carros)
       #select_img(0,1)
       
    elif(carros[i][j]<carros[i+1][j]):
       value=carros[i]
       carros[i]=carros[i+1]
       carros[i+1]=value
       return ordenar_ef(0,j)

    else:
       return ordenar_ef(i+1,j)


#-------------------------------Editar Eficiencia--------------------------

def asignar_carro(car,EF):
    global carros

    carros[0][6]=PhotoImage(file="Tesla.png")
    carros[1][6]=PhotoImage(file="Ferrari.png")
    carros[2][6]=PhotoImage(file="McL.png")
    carros[3][6]=PhotoImage(file="Porshe2.png")
    carros[4][6]=PhotoImage(file="VW.png")
    carros[5][6]=PhotoImage(file="Maserati.png")
    
    EF=EF.get()
    if(car=="Tesla"):
        carros[0][0]=EF
        ordenar_ef(0,0)
        
    elif(car=="Ferrari"):
        carros[1][0]=EF
        ordenar_ef(0,0)
        
    elif(car=="McLaren"):
        carros[2][0]=EF
        ordenar_ef(0,0)
        
    elif(car=="Porshe"):
        carros[3][0]=EF
        ordenar_ef(0,0)
        
    elif(car=="VolksWagen"):
        carros[4][1]=EF
        ordenar_ef(0,0)
        
    elif(car=="Maserati"):
        carros[5][1]=EF
        ordenar_ef(0,0)

    else:
        ''
        
        

def editar_ef():

    def close():
        v_ef.iconify()
        call()

    def select_car():
        car=SpinB_carro.get()
        asignar_carro(car,EF)
        print(car,EF.get())

    v_ef=Toplevel()
    v_ef.title("Formula-E")
    v_ef.geometry("500x400")
    v_ef.configure(background=fondo2)

    EF=IntVar()

    Lb_titulo=Label(v_ef,text="Editar Información de los Automoviles",font=("Cambria",18),fg=textomorado,background=fondo2).place(x=50,y=5)

    Lb_sel=Label(v_ef,text="Seleccione el automóvil en el que desea realizar cambios:",font=("News Gothic",12),background=fondo2).place(x=30,y=80)

    SpinB_carro=ttk.Combobox(v_ef,values=("Tesla","Ferrari","McLaren","Porshe","VolksWagen","Maserati"))
    SpinB_carro.current(0)
    SpinB_carro.place(x=40,y=120)

    Lb_ef=Label(v_ef,text="Eficiencia del Carro:",font=("News Gothic",12),background=fondo2).place(x=30,y=200)

    En_ef=Entry(v_ef,textvariable=EF).place(x=40,y=240)

    Lb_unit=Label(v_ef,text="Km/KWh",background=fondo2).place(x=175,y=237)

    Bt_Save=Button(v_ef,text="Guardar Cambios",command=select_car,width=20,height=2).place(x=30,y=350)

    Bt_seguir=Button(v_ef,text="Ver Ranking",command=close,width=20,height=2).place(x=200,y=350)


    
#editar_ef()
    

#call()




