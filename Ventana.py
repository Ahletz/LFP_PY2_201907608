from tkinter import *


class Interfaz:



    def Open(self) :
        
        raiz = Tk ()
        raiz.geometry('800x600') #tamaño de la ventana
        raiz.resizable(0,0) #comando para no redimensionar la ventana 
        raiz.configure(background='light blue') #color de la ventana
        raiz.title('Liga Bot') #nombre del bot

        self.Botones() #llamado de los botones
        self.Caja()#caja de texto
        self.Pantalla()#muestra de lo que se envia

        raiz.mainloop() #loop para que no cierre la ventana

    def Botones(self):

            ##Botones
        boton1 = Button(text='Reporte de errores',height=1,width=20).place(x=10,y=10) 
        boton2 = Button(text='Limpiador log de Errores',height=1,width=20).place(x=10,y=50) 
        boton3 = Button(text='Reporte de Tokens',height=1,width=20).place(x=10,y=90) 
        boton4 = Button(text='Limpiador log de Tokens',height=1,width=20).place(x=10,y=130) 
        boton5 = Button(text='Manual Usuario',height=1,width=20).place(x=10,y=170) 
        boton6 = Button(text='Manual técnico',height=1,width=20).place(x=10,y=210)
        boton7 = Button(text='Enviar',height=1,width=20).place(x=10,y=550)

    def Caja(self):

        caja =Entry().place(x=200,y=550,height=30,width=575) #caja de texto 

    def Pantalla(self):

        pantalla = Text(background="navajo white", width=72, height=33)
        pantalla.configure(state='disable')
        pantalla.place(x=200,y=10)

