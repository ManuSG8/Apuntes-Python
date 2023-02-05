from cgitb import text
from contextlib import nullcontext
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import tkinter
from unittest import result
from os import remove
import webbrowser

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
            miId.set(usuario[0])
            miNombre.set(usuario[1])
            miApellido.set(usuario[3])
            miPassword.set(usuario[2])
            miDireccion.set(usuario[4])
            cuadroComentarios.delete(1.0, "end") # Esto borra lo que haya en la caja de comentarios para que no se solapen
            cuadroComentarios.insert(1.0, usuario[5])
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

    else:

        messagebox.showerror("BBDD", "El registro no existe")

    miConexion.commit()

    
def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia M.A.N.U")


def infoAdicional():
    valor = messagebox.askquestion("ManuDB", "Gestor de bases de datos: ManuDB - 2022\n¿Quieres saber más?")
    if valor == "yes":
        webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')



# --------------------------- Interfaz Gráfica ---------------------------
root = Tk()
root.geometry("400x450")
root.title("Gestor BBDD")
root.resizable(False, False)
root.iconbitmap(r"C:\Users\manu-\Desktop\Python\favi.ico")
root.config(background="#454545")

miFrame = Frame(root)

miFrame.pack()

miFrame.config(bg="#454545", pady=20)

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)


# --------------------------- BBDD ---------------------------
BBDDMenu = Menu(barraMenu, tearoff=0)
BBDDMenu.add_command(label="Crear BBDD", command=conexionBBDD)
BBDDMenu.add_command(label="Eliminar BBDD", command=borrarBBDD)
BBDDMenu.add_separator()
BBDDMenu.add_command(label="Salir", command=salirAplicacion)

barraMenu.add_cascade(label="BBDD", menu=BBDDMenu)


# --------------------------- Borrar ---------------------------
borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

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
labelID = Label(miFrame, text="ID:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)
labelID.config(bg="#454545", fg="white")

miNombre = StringVar()
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, columnspan=4)
cuadroNombre.config(bg="#999999")
labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)
labelNombre.config(bg="#454545", fg="white")

miApellido = StringVar()
cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, columnspan=4)
cuadroApellido.config(bg="#999999")
labelApellido = Label(miFrame, text="Apellido:")
labelApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)
labelApellido.config(bg="#454545", fg="white")

miPassword = StringVar()
cuadroPassword = Entry(miFrame, textvariable=miPassword)
cuadroPassword.grid(row=3, column=1, columnspan=4)
cuadroPassword.config(bg="#999999",show="*")
labelPassword = Label(miFrame, text="Password:")
labelPassword.grid(row=3, column=0, sticky="e", padx=10, pady=10)
labelPassword.config(bg="#454545", fg="white")

miDireccion = StringVar()
cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, columnspan=4)
cuadroDireccion.config(bg="#999999")
labelDireccion = Label(miFrame, text="Dirección:")
labelDireccion.grid(row=4, column=0, sticky="e", padx=10, pady=10)
labelDireccion.config(bg="#454545", fg="white")

# Aquí no es necesario el miComentario = StringVar() ni el textvariable = miComentario
cuadroComentarios = Text(miFrame, width=15, height=5)
cuadroComentarios.grid(row=5, column=1, pady=10, columnspan=4)
scrollVertical = Scrollbar(miFrame, command=cuadroComentarios.yview) 
scrollVertical.grid(row=5, column=6, sticky="nsew", padx=10, pady=5) 
cuadroComentarios.config(bg="#999999",yscrollcommand=scrollVertical.set)
labelComentarios = Label(miFrame, text="Comentarios:")
labelComentarios.grid(row=5, column=0, sticky="e", padx=10, pady=10)
labelComentarios.config(bg="#454545", fg="white")


# --------------------------- Botones ---------------------------
miFrame2 = Frame(root)
miFrame2.pack()
miFrame2.config(background="#454545")

botonCreate = ttk.Button(miFrame2, text="Create", width=7, command=crear)
botonCreate.grid(row=0, column=0, padx=10, pady=10)

botonRead = ttk.Button(miFrame2, text="Read", width=7, command=leer)
botonRead.grid(row=0, column=1, padx=10, pady=10)

botonUpdate = ttk.Button(miFrame2, text="Update", width=7, command=actualizar)
botonUpdate.grid(row=0, column=2, padx=10, pady=10)

botonDelete = ttk.Button(miFrame2, text="Delete", width=7, command=eliminarRegistro)
botonDelete.grid(row=0, column=3, padx=10, pady=10)


root.mainloop()