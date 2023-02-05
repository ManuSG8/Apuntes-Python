# WIDGET PARA MOSTRAR TEXTO O IMÁGENES
# No se puede interactuar con él (borrar, arrastrar, etc)
# Sintaxis: variableLabel = Label(contenedor, opciones)


""" from tkinter import *

root = Tk() # Raíz

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miImagen = PhotoImage(file="hamburguesa.png")

miLabel = Label(miFrame, text="Hola alumnos de Python", fg="blue", font=("Comic Sans MS", 25))

miLabel.place(x=100, y= 200) # Nos permite ubicar el texto en cualquier lugar de la GUI

root.mainloop() """



#miLabel = Label(miFrame, text="Hola alumnos de Python")
#miLabel.place(x=100, y= 200)
# Estas 2 líneas se pueden abreviar de la siguiente forma si no vamos a usar más la variable de tipo Label
#Label(miFrame, text="Hola alumnos de Python").place(x=100, y= 200)


from tkinter import *

root = Tk() # Raíz

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miImagen = PhotoImage(file=r"C:\Users\Manuel\Desktop\Python\interfaces_graficas\hamburguesa.png") # Debería funcionar...

miLabel = Label(miFrame, image=miImagen)

miLabel.place(x=100, y= 200) # Nos permite ubicar el texto en cualquier lugar de la GUI

root.mainloop()