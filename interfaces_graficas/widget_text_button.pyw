# WIDGETS TEXT Y BUTTON
# Widget text: introducir mucho texto
# Widget button: un botón


from tkinter import *

raiz = Tk()

raiz.geometry("1080x720")

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre = StringVar() # Le decimos que se trata de una cadena de caracteres

cuadroNombre = Entry(miFrame, textvariable=minombre) # Le decimos que va a estar asociado con el valor de esa variable, que lo asignamos al pulsar el botón de "Enviar"
cuadroNombre.grid(row=0, column=1) 
cuadroNombre.config(fg="blue", justify="center") 

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=1, column=1)
cuadroPassword.config(show="*") 

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

textoComentario = Text(miFrame, width=16, height=5) # Le damos un tamaño razonable, porque por defecto es muy grande
textoComentario.grid(row=4, column=1, pady=15, padx=5)

scrollVertical = Scrollbar(miFrame, command=textoComentario.yview) # Creamos la barra de scroll del textoComentario. yview significa que funciona de manera vertical
scrollVertical.grid(row=4, column=2, sticky="nsew") # Fíjate bien como está posicionado. Además lo adaptamos al tamaño del bloque de texto
textoComentario.config(yscrollcommand=scrollVertical.set) # Adapta el tamaño a la cantidad de texto y se mantiene en la posición

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", pady=15, padx=5) 

passwordLabel = Label(miFrame, text="Password: ")
passwordLabel.grid(row=1, column=0, sticky="e", pady=15, padx=5)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", pady=15, padx=5)

direccionLabel = Label(miFrame, text="Direccion: ") 
direccionLabel.grid(row=3, column=0, sticky="e", pady=15, padx=5)

comentariosLabel = Label(miFrame, text="Comentarios: ") 
comentariosLabel.grid(row=4, column=0, sticky="e", pady=15, padx=5)

def codigoBoton():
    minombre.set("Juan")

botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()

raiz.mainloop()