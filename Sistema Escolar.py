#Sistema Escolar
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

#No puede
def crearventana():
    ventana2=tk.Tk()
    ventana2.title("Resultados")
    tabControl2 = ttk.Notebook(ventana2)
    tab3 = ttk.Frame(tabControl2)
    tabControl2.add(tab3, text='Datos Personales')
    tabControl2.pack(expand=1,fill="both")
    tskinomi = ttk.Label(tab3,text=nombre.get()+"\n"+apellido1.get()+"\n"+apellido2.get()+"\n"+direccion.get()+"\n"+colonia.get()+"\n"+ciudad.get()+"\n"+municipio.get())
    tskinomi.grid(column=5,row=1)
    tab4 = ttk.Frame(tabControl2)
    tabControl2.add(tab4,text='Extras')
    x=""
    if opcion_1.get()==1:
        x=x+"\n     -Leer"
    if opcion_2.get()==1:
        x=x+"\n     -Peliculas"
    if opcion_3.get()==1:
        x=x+"\n     -Redes sociales"
    if opcion_1.get()==0 and opcion_2.get()==0 and opcion_3.get()==0:
        x=x+"No tienes pasatiempos"
        x=x+"\n Estado civil: "
    if opcion.get()==1:
        x=x+"\nSoltero"
    if opcion.get()==2:
        x=x+"\nViudo"
    if opcion.get()==3:
        x=x+"\nCasado"
        x=x+"\nObjetivos de la vida: "
    if obj.get('1.0',tk.END)=="\n":
        x=x+" \nNo tines objetivos en la vida"
    else:    
        x=x+obj.get('1.0',tk.END)
    tskinomi2 = ttk.Label(tab4,text=x)
    tskinomi2.grid(column=5,row=2)
    ventana2.mainloop()
def funcion_caja_mensaje():
    mBox.showinfo('Informacion de ayuda','Para mayor soporte contactar a Riemaru Karurosu')
def click():
    if nombre.get() !="" and apellido1.get() !="" and apellido2.get() !="" and direccion.get() !="":
        crearventana()
    else:
        definicion='Debe llenar los datos'
    texter=ttk.Label(tab1,text=definicion)
    texter.grid(column=5,row=21)
    texter=ttk.Label(tab2,text=definicion)
    texter.grid(column=5,row=21)
def click2():
    if opcion_1!="" and opcion_2!="" and opcion_3!="" and opcion!="":
        click()
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()
ventana=tk.Tk()
ventana.title("Sistema Escolar")

#tab1
tabControl = ttk.Notebook(ventana)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Datos Personales')
tabControl.pack(expand=1,fill="both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text='Extras')

texto=ttk.Label(tab1,text="Nombre: ")
texto.grid(column=0,row=0)
nombre=tk.StringVar()
preguntar_nombre=ttk.Entry(tab1,width=20,textvariable=nombre)
preguntar_nombre.grid(column=1,row=0)

texto=ttk.Label(tab1,text="Apellido Paterno: ")
texto.grid(column=0,row=2)
apellido1=tk.StringVar()
preguntar_apellido1=ttk.Entry(tab1,width=20,textvariable=apellido1)
preguntar_apellido1.grid(column=1,row=2)

texto=ttk.Label(tab1,text="Apellido Materno: ")
texto.grid(column=0,row=4)

apellido2=tk.StringVar()
preguntar_apellido2=ttk.Entry(tab1,width=20,textvariable=apellido2)
preguntar_apellido2.grid(column=1,row=4)

texto=ttk.Label(tab1,text="Dirección: ")
texto.grid(column=0,row=6)

direccion=tk.StringVar()
preguntar_direccion=ttk.Entry(tab1,width=20,textvariable=direccion)
preguntar_direccion.grid(column=1,row=6)

texto=ttk.Label(tab1,text="Colonia: ")
texto.grid(column=0,row=8)

colonia=tk.StringVar()
seleccionar_numero=ttk.Combobox(tab1,width=12, textvariable=colonia)
seleccionar_numero['values'] = ("Felix Ireta","Villa Universidad","Felicitas del Rio")
seleccionar_numero.grid(column=1,row=8)
seleccionar_numero.current(0)

texto=ttk.Label(tab1,text="Ciudad: ")
texto.grid(column=0,row=10)

ciudad=tk.StringVar()
seleccionar_numero=ttk.Combobox(tab1,width=12, textvariable=ciudad)
seleccionar_numero['values'] = ("Morelia","Ciudad de Mexico","Estado de Mexico")
seleccionar_numero.grid(column=1,row=10)
seleccionar_numero.current(0)


texto=ttk.Label(tab1,text="Municipio: ")
texto.grid(column=0,row=13)

municipio=tk.StringVar()
seleccionar_numero=ttk.Combobox(tab1,width=12, textvariable=municipio)
seleccionar_numero['values'] = ("Morelia","Atzcapotzalco","Toluca")
seleccionar_numero.grid(column=1,row=13)
seleccionar_numero.current(0)

texto=ttk.Label(tab2,text="Pasatiempos")
texto.grid(column=0,row=17)

#Botón de control
opcion_1= tk.IntVar()
casilla_1=tk.Checkbutton(tab2,text="Videojuegos",variable=opcion_1)
casilla_1.select()
casilla_1.grid(column=1,row=18,sticky=tk.W)

#Botón de control 2
opcion_2= tk.IntVar()
casilla_2=tk.Checkbutton(tab2,text="Leer",variable=opcion_2)
casilla_2.select()
casilla_2.grid(column=0,row=18,sticky=tk.W)

#Botón de control 3
opcion_3= tk.IntVar()
casilla_3=tk.Checkbutton(tab2,text="Comer",variable=opcion_3)
casilla_3.select()
casilla_3.grid(column=2,row=18,sticky=tk.W)

#Radio 1
opcion = tk.IntVar()
radio1 = tk.Radiobutton(tab2,text="Soltero", variable=opcion,value=1)
radio1.grid(column=0,row=19,sticky=tk.W)

#Radio 2
radio2 = tk.Radiobutton(tab2,text="Viudo", variable=opcion,value=2)
radio2.grid(column=1,row=19,sticky=tk.W)

#Radio 3
radio3 = tk.Radiobutton(tab2,text="Casado", variable=opcion,value=3)
radio3.grid(column=2,row=19,sticky=tk.W)

texto11=ttk.Label(tab2,text="Objetivo de la vida:").grid(column=0,row=4)
obj=scrolledtext.ScrolledText(tab2,width=30,height=3,wrap=tk.WORD)
obj.grid(column=0,columnspan=3)

#Boton
accion=ttk.Button(tab1,text="Imprimir datos",command=click)
accion.grid(column=5,row=20)
#Boton 2
accion=ttk.Button(tab2,text="Imprimir datos",command=click2)
accion.grid(column=5,row=20)
#Menu
barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
#Agregar opciones al menu
opciones_menu = Menu(barra_menu)
opciones_menu.add_command(label="Imprimir",command=click)
opciones_menu.add_command(label="Salir",command=funcion_salir)
barra_menu.add_cascade(label="Archivo",menu=opciones_menu)

#Menu ayuda, opcion 2
menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de",command=funcion_caja_mensaje)
barra_menu.add_cascade(label="Ayuda",menu=menu_ayuda)

ventana.mainloop()