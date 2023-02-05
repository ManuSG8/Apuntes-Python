from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0) # Con tearoff elimina el separador por defecto
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator() # Crea una barra divisora
archivoMenu.add_command(label="Salir")

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barraMenu, tearoff=0)
# Lo dejamos vacío porque sí, porque queremos

archivoAyuda = Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()