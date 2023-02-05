# https://docs.python.org/3/library/tk.html

# IMPORTANTE: el nombre del archivo lleva la extensión pyw para que no nos abra la terminal, sólo queremos que se abra la ventana de la aplicación

""" from tkinter import *

raiz = Tk()

raiz.mainloop() # Es un bucle infinito que mantiene la ventana abierta
# Con estas 3 lineas creamos la ventana """



from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(True, True) # Permite dos parámetros de tipo boolean. El primero corresponde al width y el segundo al height. Nos permite limitar el uso de redimensionar Prueba con (False, True) por ejemplo

raiz.iconbitmap(r"C:\Users\manu-\Desktop\Python\interfaces_graficas\favicon.ico") # Cambiar favicon

raiz.geometry("650x350") # Cambia el tamaño de la ventana por defecto

raiz.config(bg="blue") # Este método nos permitirá hacer muchas cosas, como por ejemplo, cambiar el color del fondo

raiz.mainloop() # Debe estar siempre al final