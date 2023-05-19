#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------
import tkinter as tk
from tkinter import ttk
# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel personales
def abrir_toplevel_personales():
    global toplevel_personales
    toplevel_personales = Toplevel()
    toplevel_personales.title("personales")
    toplevel_personales.resizable(False, False)
    toplevel_personales.geometry("300x200")
    toplevel_personales.config(bg="white")

    # text peso
    lb_c = Label(toplevel_personales, text = "nombre")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=60)

        #caja de text peso
    entradaTextos = ttk.Entry(toplevel_personales, width=30, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=100,y=60)



        # text peso
    lb_c = Label(toplevel_personales, text = "grado")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=30)
   
    #caja de text peso
    entradaTextos = ttk.Entry(toplevel_personales, width=30, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=100,y=30)

            # text peso
    lb_c = Label(toplevel_personales, text = "correo")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=0)
   
    #caja de text peso
    entradaTextos = ttk.Entry(toplevel_personales, width=30, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=100,y=0)

                # text peso
    lb_c = Label(toplevel_personales, text = "sede")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=90)
   
    #caja de text peso
    entradaTextos = ttk.Entry(toplevel_personales, width=30, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=100,y=90)

                    # text peso
    lb_c = Label(toplevel_personales, text = "telfono")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=120)
   
    #caja de text peso
    entradaTextos = ttk.Entry(toplevel_personales, width=30, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=100,y=120)

       # boton para convertir
    bt_aceptar = Button(toplevel_personales,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)




# aceptar
def aceptar():
    global cent
    cent = int(personales.get())
    toplevel_personales.destroy()




# abrir toplevel academicos
def abrir_toplevel_academicos():
    global toplevel_academicos
    toplevel_academicos = Toplevel()
    toplevel_academicos.title("academicos")
    toplevel_academicos.resizable(False, False)
    toplevel_academicos.geometry("300x200")
    toplevel_academicos.config(bg="white")


    # text peso
    lb_c = Label(toplevel_academicos, text = "actitudinal 10%")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=0)

        #caja de text peso
    entradaTextos = ttk.Entry(toplevel_academicos, width=10, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=200,y=0)

        # text peso
    lb_c = Label(toplevel_academicos, text = "autoevaluacion 10%")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=30)

        #caja de text peso
    entradaTextos = ttk.Entry(toplevel_academicos, width=10, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=200,y=30)

            # text peso
    lb_c = Label(toplevel_academicos, text = "bimestral 20%")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=60)

        #caja de text peso
    entradaTextos = ttk.Entry(toplevel_academicos, width=10, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=200,y=60)

                # text peso
    lb_c = Label(toplevel_academicos, text = "procedimental 30%")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=90)

        #caja de text peso
    entradaTextos = ttk.Entry(toplevel_academicos, width=10, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=200,y=90)

                    # text peso
    lb_c = Label(toplevel_academicos, text = "cognitivo 30%")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=120)

        #caja de text peso
    entradaTextos = ttk.Entry(toplevel_academicos, width=10, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=200,y=120)




# abrir toplevel IMC
def abrir_toplevel_IMC():
    global toplevel_IMC
    toplevel_IMC = Toplevel()
    toplevel_IMC.title("IMC")
    toplevel_IMC.resizable(False, False)
    toplevel_IMC.geometry("300x200")
    toplevel_IMC.config(bg="white")

        #caja de text peso
    entradaTextos = ttk.Entry(toplevel_IMC, width=30, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=100,y=0)

    # text peso
    lb_c = Label(toplevel_IMC, text = "peso")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=0)

    # text peso
    lb_c = Label(toplevel_personales, text = "altura")
    lb_c.config(bg="white", fg="black", font=("Helvetica", 18))
    lb_c.place(x=10, y=30)

    #caja de text peso
    entradaTextos = ttk.Entry(toplevel_academicos, width=30, justify=tk.CENTER)
    entradaTextos.grid(row=0, column=4)
    entradaTextos.place(x=100,y=30)

# boton para convertir
    bt_aceptar = Button(toplevel_academicos,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)


# aceptar
def aceptar():
    global cent
    cent = int(academicos.get())
    toplevel_academicos.destroy()







    # logo de la app
    lb_logo2 = Label(toplevel_personales, image=logo, bg="white")
    lb_logo2.place(x=10,y=10)



   # boton para convertir
    bt_aceptar = Button(toplevel_personales,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)




   # boton para convertir
    bt_aceptar = Button(toplevel_personales,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)


# aceptar
def aceptar():
    global cent
    cent = int(personales.get())
    toplevel_personales.destroy()






# aceptar
def aceptar():
    messagebox.showinfo("personales", "La app se va a cerrar")
    toplevel_personales.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("ANDRES TARAZONA")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="white")

# variables principales
global imc
global img
global personales
global IMC
global academicos
toplevel_imc=StringVar
toplevel_img=StringVar
toplevel_personales=Text
toplevel_IMC=Text
toplevel_academicos=Text
#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=500, height=500)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="INF PERSONAL")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# boton para abrir Toplevel para ingresar personales
bt_centigrados = Button(frame_entrada,  text="datos academicos", command=abrir_toplevel_personales)
bt_centigrados.place(x=240, y=60)



# boton para abrir Toplevel para ingresar academicos
bt_centigrados = Button(frame_entrada, text="Ingresar datos", command=abrir_toplevel_academicos)
bt_centigrados.config(bg="white", width=20, height=8)
bt_centigrados.place(x=40, y=300)

# boton para abrir Toplevel para ingresar IMC
bt_centigrados = Button(frame_entrada, text="Ingresar IMC", command=abrir_toplevel_IMC)
bt_centigrados.config(bg="white", width=20, height=8)
bt_centigrados.place(x=240, y=300)

#----------------
#framemedio------
#----------------
#-----------------------------------
frame_medio = Frame(ventana_principal)
frame_medio.config(bg="ivory3", width=480, height=480)
frame_medio.place(x=10, y=200)

#imagenes delos botones
imc=PhotoImage(file="imc.png")
img=PhotoImage(file="img.png")

#boton sobre la imc
bt_imc= Button(frame_medio,image=imc, command=abrir_toplevel_IMC)
bt_imc.place(x=40, y=150 , width=130, height=125)
bt_imc.config(bg="indianred1")

#boton para academicos
bt_academicos= Button(frame_medio,image=img, command=abrir_toplevel_academicos)
bt_academicos.place(x=300, y=150 , width=130, height=130,)
bt_academicos.config(bg="white")






# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()