from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(True, True)

raiz.iconbitmap(r"C:\Users\Manuel\Desktop\Python\interfaces_graficas\favicon.ico") 

raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame = Frame() # Creamos el frame, pero es necesario empaquetarlo (meterlo en la raíz) y darle tamaño

miFrame.pack(side="right", anchor="s") # Lo empaquetamos y le podemos pasar parámetros para posicionarlo. El método anchor usa puntos cardinales (n,e,w,s)

#miFrame.pack(fill="both", expand="True") # Prueba con miFrame.pack(fill="y", expand="True") - miFrame.pack(fill="x")

miFrame.config(width="650", height="350") # Los frames tienen un tamaño fijo

miFrame.config(bg="red") # Le cambiamos el color

miFrame.config(bd=35)
miFrame.config(relief="raised") # Estas 2 lineas cambian el borde del frame

miFrame.config(cursor="pirate") # Cambia el icono del cursor cuando pasa por encima del frame

# Todo lo aplicado al frame, se le puede aplicar a la raíz

raiz.config(bd=20)
raiz.config(relief="sunken") 

raiz.config(cursor="hand2")

raiz.mainloop()