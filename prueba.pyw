from cgitb import text
from contextlib import nullcontext
from mimetypes import common_types
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import tkinter
from turtle import right
from unittest import result
from os import remove
import webbrowser

from setuptools import Command

# --------------------------- Funciones ---------------------------

def conexionBBDD():

    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE datosusuarios (
                id INTEGER PRIMARY KEY,
                nombre_usuario VARCHAR(50),
                password VARCHAR(50),
                apellido VARCHAR(50),
                direccion VARCHAR(50),
                comentarios VARCHAR(100)
            )
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")


def borrarBBDD():
    valor = messagebox.askquestion("Eliminar BBDD","¿Estás seguro de que deseas eliminar la Base de Datos?")
    if valor=="yes":
        try:
            remove(r"C:\Users\manu-\Desktop\Python\usuarios")
        except:
            messagebox.showwarning("¡Atención!", "La BBDD no existe")


def salirAplicacion():
    valor = messagebox.askquestion("Salir","¿Estás seguro de que quieres salir?")
    if valor=="yes":
        root.destroy()


def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPassword.set("")
    miDireccion.set("")
    cuadroComentarios.delete(1.0, END)


def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    valor = messagebox.askquestion("Insertar registro","¿Desea insertar el registro?")

    if valor == "yes":

        try:
            miCursor.execute("INSERT INTO datosusuarios VALUES ('" + miId.get() + 
            "','" + miNombre.get() +
            "','" + miPassword.get() +
            "','" + miApellido.get() +
            "','" + miDireccion.get() +
            "','" + cuadroComentarios.get("1.0", END) + "')")

            miConexion.commit()
            messagebox.showinfo("BBDD", "Registro insertado con éxito")
        except:
            messagebox.showerror("BBDD", "El registro no se pudo insertar")


def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM datosusuarios WHERE id=" + miId.get())

    elUsuario = miCursor.fetchall()

    if elUsuario:
        
        for usuario in elUsuario:
            crearFrame()            
            miId2.set(usuario[0])
            miNombre2.set(usuario[1])
            miApellido2.set(usuario[3])
            miPassword2.set(usuario[2])
            miDireccion2.set(usuario[4])
            cuadroComentarios2.delete(1.0, "end") 
            cuadroComentarios2.insert(1.0, usuario[5])
            
    else:
        messagebox.showerror("BBDD", "El registro no existe")
        
    miConexion.commit()


def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM datosusuarios WHERE id=" + miId.get())

    valor = miCursor.fetchall()

    if valor:
        
        aviso = messagebox.askquestion("Actualizar registro", "¿Estás seguro de que quieres actualizar el registro?")

        if aviso == "yes":

            miCursor.execute("UPDATE datosusuarios SET id='" + miId.get()+
            "', nombre_usuario='" + miNombre.get() + 
            "', password='" + miPassword.get() + 
            "', apellido='" + miApellido.get() + 
            "', direccion='" + miDireccion.get() + 
            "', comentarios='" + cuadroComentarios.get("1.0", END) + 
            "' WHERE id=" + miId.get())

            messagebox.showinfo("BBDD", "Registro actualizado con éxito")

            miId2.set(miId.get())
            miNombre2.set(miNombre.get())
            miApellido2.set(miApellido.get())
            miPassword2.set(miPassword.get())
            miDireccion2.set(miDireccion.get())
            cuadroComentarios2.delete(1.0, "end") 
            cuadroComentarios2.insert(1.0, cuadroComentarios.get("1.0", END))

    else:

        messagebox.showerror("BBDD", "El registro que intentas actualizar no existe")

    miConexion.commit()


def eliminarRegistro():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM datosusuarios WHERE id=" + miId.get())

    valor = miCursor.fetchall()

    if valor:   

        aviso = messagebox.askquestion("Eliminar registro", "¿Estás seguro de que quieres eliminar el registro?")

        if aviso == "yes":

            miCursor.execute("DELETE FROM datosusuarios WHERE id=" + miId.get())
            messagebox.showinfo("BBDD", "Registro eliminado con éxito")
            limpiarCampos()
            limpiarLectura()

    else:

        messagebox.showerror("BBDD", "El registro no existe")

    miConexion.commit()


def realizarCambios():
    miId.set(miId2.get())
    miNombre.set(miNombre2.get())
    miApellido.set(miApellido2.get())
    miPassword.set(miPassword2.get())
    miDireccion.set(miDireccion2.get())
    cuadroComentarios.delete(1.0, "end") 
    cuadroComentarios.insert(1.0, cuadroComentarios2.get("1.0", END))


def limpiarLectura():
    miId2.set("")
    miNombre2.set("")
    miApellido2.set("")
    miPassword2.set("")
    miDireccion2.set("")
    cuadroComentarios2.delete(1.0, END)


def limpiarTotal():
    limpiarCampos()
    limpiarLectura()


def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia M.A.N.U")


def infoAdicional():
    valor = messagebox.askquestion("ManuDB", "Gestor de bases de datos: ManuDB - 2022\n¿Quieres saber más?")
    if valor == "yes":
        webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')


def crearFrame():
    global miFrame3
    miFrame3 = Frame()
    miFrame3.pack(side="right", anchor="n")
    miFrame3.config(background="#454545")
    miFrame3.config(width="1900", height="900", padx=500, pady=80)

    global miFrame4
    miFrame4 = Frame(miFrame3)
    miFrame4.pack(side="left", anchor="n")
    miFrame4.config(background="#454545", pady=0, padx=40)
    miFrame4.config(bd=5, relief="solid")

    global miId2
    miId2 = StringVar()
    cuadroID2 = Entry(miFrame4, textvariable=miId2)
    cuadroID2.grid(row=0, column=1, columnspan=4)
    cuadroID2.config(bg="#999999")
    labelID2 = Label(miFrame4, text="ID:", font="Tahoma 12 italic italic")
    labelID2.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    labelID2.config(bg="#454545", fg="white")

    global miNombre2
    miNombre2 = StringVar()
    cuadroNombre2 = Entry(miFrame4, textvariable=miNombre2)
    cuadroNombre2.grid(row=1, column=1, columnspan=4)
    cuadroNombre2.config(bg="#999999")
    labelNombre2 = Label(miFrame4, text="Nombre:", font="Tahoma 12 italic")
    labelNombre2.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    labelNombre2.config(bg="#454545", fg="white")

    global miApellido2 
    miApellido2= StringVar()
    cuadroApellido2 = Entry(miFrame4, textvariable=miApellido2)
    cuadroApellido2.grid(row=2, column=1, columnspan=4)
    cuadroApellido2.config(bg="#999999")
    labelApellido2 = Label(miFrame4, text="Apellido:", font="Tahoma 12 italic")
    labelApellido2.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    labelApellido2.config(bg="#454545", fg="white")

    global miPassword2
    miPassword2 = StringVar()
    cuadroPassword2 = Entry(miFrame4, textvariable=miPassword2)
    cuadroPassword2.grid(row=3, column=1, columnspan=4)
    cuadroPassword2.config(bg="#999999",show="*")
    labelPassword2 = Label(miFrame4, text="Password:", font="Tahoma 12 italic")
    labelPassword2.grid(row=3, column=0, sticky="e", padx=10, pady=10)
    labelPassword2.config(bg="#454545", fg="white")

    global miDireccion2
    miDireccion2 = StringVar()
    cuadroDireccion2 = Entry(miFrame4, textvariable=miDireccion2)
    cuadroDireccion2.grid(row=4, column=1, columnspan=4)
    cuadroDireccion2.config(bg="#999999")
    labelDireccion2 = Label(miFrame4, text="Dirección:", font="Tahoma 12 italic")
    labelDireccion2.grid(row=4, column=0, sticky="e", padx=10, pady=10)
    labelDireccion2.config(bg="#454545", fg="white")

    # Aquí no es necesario el miComentario = StringVar() ni el textvariable = miComentario
    global cuadroComentarios2
    cuadroComentarios2 = Text(miFrame4, width=15, height=5)
    cuadroComentarios2.grid(row=5, column=1, pady=10, columnspan=4)
    scrollVertical2 = Scrollbar(miFrame4, command=cuadroComentarios.yview) 
    scrollVertical2.grid(row=5, column=6, sticky="nsew", padx=10, pady=5) 
    cuadroComentarios2.config(bg="#999999",yscrollcommand=scrollVertical.set)
    labelComentarios2 = Label(miFrame4, text="Comentarios:", font="Tahoma 12 italic")
    labelComentarios2.grid(row=5, column=0, sticky="e", padx=10, pady=10)
    labelComentarios2.config(bg="#454545", fg="white")

    botonRCambios = ttk.Button(miFrame4, text="Realizar Cambios", width=16, command=realizarCambios)
    botonRCambios.grid(row=6, column=0, padx=20, pady=20)

    botonLimpiar = ttk.Button(miFrame4, text="Limpiar Campos", width=16, command=limpiarLectura)
    botonLimpiar.grid(row=6, column=1, padx=20, pady=20)



def borrarFrame():
    global miFrame4
    miFrame4.destroy()


# --------------------------- Interfaz Gráfica ---------------------------
root = Tk()
root.geometry("1920x1080")
root.title("Gestor BBDD")
root.resizable(True, True)
root.iconbitmap(r"C:\Users\manu-\Desktop\Python\favi.ico")
root.config(background="#454545")

miFrame = Frame(root)

miFrame.config(width="1900", height="900")

miFrame.pack(side="left", anchor="n")

miFrame.config(bg="#454545", pady=80, padx=80)

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)


# --------------------------- BBDD ---------------------------
BBDDMenu = Menu(barraMenu, tearoff=0)
BBDDMenu.add_command(label="Crear BBDD", command=conexionBBDD)
BBDDMenu.add_command(label="Eliminar BBDD", command=borrarFrame)
BBDDMenu.add_separator()
BBDDMenu.add_command(label="Salir", command=salirAplicacion)

barraMenu.add_cascade(label="BBDD", menu=BBDDMenu)


# --------------------------- Borrar ---------------------------
borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos del formulario", command=limpiarCampos)
borrarMenu.add_command(label="Borrar campos de la ventana", command=limpiarLectura)
borrarMenu.add_command(label="Borrar todos los campos", command=limpiarTotal)

barraMenu.add_cascade(label="Borrar", menu=borrarMenu)


# --------------------------- CRUD ---------------------------
CRUDMenu = Menu(barraMenu, tearoff=0)
CRUDMenu.add_command(label="Create", command=crear)
CRUDMenu.add_command(label="Read", command=leer)
CRUDMenu.add_command(label="Update", command=actualizar)
CRUDMenu.add_command(label="Delete", command=eliminarRegistro)

barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)


# --------------------------- Ayuda ---------------------------
ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# --------------------------- Entry data ---------------------------
miId = StringVar()
cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, columnspan=4)
cuadroID.config(bg="#999999")
labelID = Label(miFrame, text="ID:", font="Tahoma 12 italic italic")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)
labelID.config(bg="#454545", fg="white")

miNombre = StringVar()
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, columnspan=4)
cuadroNombre.config(bg="#999999")
labelNombre = Label(miFrame, text="Nombre:", font="Tahoma 12 italic")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)
labelNombre.config(bg="#454545", fg="white")

miApellido = StringVar()
cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, columnspan=4)
cuadroApellido.config(bg="#999999")
labelApellido = Label(miFrame, text="Apellido:", font="Tahoma 12 italic")
labelApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)
labelApellido.config(bg="#454545", fg="white")

miPassword = StringVar()
cuadroPassword = Entry(miFrame, textvariable=miPassword)
cuadroPassword.grid(row=3, column=1, columnspan=4)
cuadroPassword.config(bg="#999999",show="*")
labelPassword = Label(miFrame, text="Password:", font="Tahoma 12 italic")
labelPassword.grid(row=3, column=0, sticky="e", padx=10, pady=10)
labelPassword.config(bg="#454545", fg="white")

miDireccion = StringVar()
cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, columnspan=4)
cuadroDireccion.config(bg="#999999")
labelDireccion = Label(miFrame, text="Dirección:", font="Tahoma 12 italic")
labelDireccion.grid(row=4, column=0, sticky="e", padx=10, pady=10)
labelDireccion.config(bg="#454545", fg="white")

# Aquí no es necesario el miComentario = StringVar() ni el textvariable = miComentario
cuadroComentarios = Text(miFrame, width=15, height=5)
cuadroComentarios.grid(row=5, column=1, pady=10, columnspan=4)
scrollVertical = Scrollbar(miFrame, command=cuadroComentarios.yview) 
scrollVertical.grid(row=5, column=6, sticky="nsew", padx=10, pady=5) 
cuadroComentarios.config(bg="#999999",yscrollcommand=scrollVertical.set)
labelComentarios = Label(miFrame, text="Comentarios:", font="Tahoma 12 italic")
labelComentarios.grid(row=5, column=0, sticky="e", padx=10, pady=10)
labelComentarios.config(bg="#454545", fg="white")


# --------------------------- Botones ---------------------------
miFrame2 = Frame(root)
miFrame2.pack(side="left", anchor="n")
miFrame2.config(background="#454545", pady=80)

botonCreate = ttk.Button(miFrame2, text="Create", width=7, command=crear)
botonCreate.grid(row=0, column=0, padx=20, pady=20)

botonRead = ttk.Button(miFrame2, text="Read", width=7, command=leer)
botonRead.grid(row=1, column=0, padx=20, pady=20)

botonUpdate = ttk.Button(miFrame2, text="Update", width=7, command=actualizar)
botonUpdate.grid(row=2, column=0, padx=20, pady=20)

botonDelete = ttk.Button(miFrame2, text="Delete", width=7, command=eliminarRegistro)
botonDelete.grid(row=3, column=0, padx=20, pady=20)



# --------------------------- Bucle Aplicación ---------------------------
root.mainloop()