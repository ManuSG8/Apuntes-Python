# TÍPICO CUADRO DE TEXTO

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1) # Crear casillas, como una tabla, para facilitar la disposición de varios elementos
cuadroNombre.config(fg="blue", justify="center") # Al escribir el texto aparece en azul y centrado

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=1, column=1)
cuadroPassword.config(show="*") # Como ocultar el texto, por ejemplo en una contraseña. A una base de datos, obviamente va el texto correcto, no los asteriscos o el caracter que pongas para ocultarlo

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", pady=15, padx=5) # e de East

passwordLabel = Label(miFrame, text="Password: ")
passwordLabel.grid(row=1, column=0, sticky="e", pady=15, padx=5)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", pady=15, padx=5)

direccionLabel = Label(miFrame, text="Direccion de casa: ") # Fíjate lo que pasa cuando un texto es más largo. Por defecto tienen un alineación central. Podemos modificarlo con la propiedad "sticky"
direccionLabel.grid(row=3, column=0, sticky="e", pady=15, padx=5)


raiz.mainloop()