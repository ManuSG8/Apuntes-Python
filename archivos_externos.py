# TRABAJO CON ARCHIVOS EXTERNOS

# Necesitaremos el módulo "io" de la biblioteca estándar de Python. https://docs.python.org/3/library/io.html


from io import open # De momento solo necesitamos el método open

# Modo escritura (w)

#archivo_texto = open(r"C:\Users\Manuel\Desktop\Python\archivo.txt","w") # Sintaxis de open: open(archivo,como lo vamos a abrir). Si no existe, lo crea. En VS Code tenemos que poner la ruta completa, con la r

#frase = "Estupendo día para estudiar Python \n el miércoles"

#archivo_texto.write(frase) # Volcar el contenido de una variable en un archivo

#archivo_texto.close() # Debemos cerrar el archivo



# Modo lectura (r)

#archivo_texto = open(r"C:\Users\Manuel\Desktop\Python\archivo.txt","r")

#texto = archivo_texto.read() # También existe el método readlines(), que lee línea a línea y lo almacena en una lista

#archivo_texto.close() # Debemos cerrar el archivo

#print(texto)



# Método readlines. Lee línea a línea y lo almacena en una lista

#archivo_texto = open(r"C:\Users\Manuel\Desktop\Python\archivo.txt","r")

#lineas_texto = archivo_texto.readlines()

#archivo_texto.close()

#print(lineas_texto)
#print(lineas_texto[0]) # Accedemos al primer elemento, como en una lista cualquiera

#for i in lineas_texto: # También se puede combinar con bucles y demás cosas. Como cualquier lista
#    print(i)



# Como abrir un archivo para agregar información

#archivo_texto = open(r"C:\Users\Manuel\Desktop\Python\archivo.txt","a") # "a" de append

#archivo_texto.write("\n siempre es una buena ocasión para estudiar Python")

#archivo_texto.close()



# Punteros. Método seek(): nos pedirá un parámetro que es el lugar donde queremos que se sitúe el puntero

#archivo_texto = open(r"C:\Users\Manuel\Desktop\Python\archivo.txt","r")

#print(archivo_texto.read())
#print(archivo_texto.read()) # No nos imprime 2 veces el mensaje porque el cursor llegó al final en el anterior print()

#archivo_texto.seek(0) # Desplaza el puntero al principio, posición 0
#print(archivo_texto.read())

#print("\n")
#archivo_texto.seek(17)
#print(archivo_texto.read())
#print("\n")

#archivo_texto.seek(0)
#print(archivo_texto.read(12)) # Hace una lectura hasta donde le digamos
#print("\n")
#print(archivo_texto.read()) # Leerá desde la posición 11, porque en el print() anterior, quedó ahí
#print("\n")

#archivo_texto.seek(len(archivo_texto.read())/2) # Pone el cursor en la mitad del archivo de texto
#print(archivo_texto.read())

#archivo_texto.seek(len(archivo_texto.readline())) # Lo sitúa al final de la primera línea
#print(archivo_texto.read())



# Modo lectura y escritura

#archivo_texto = open(r"C:\Users\Manuel\Desktop\Python\archivo.txt","r+") # Con r+ significa lectura y escritura

#archivo_texto.write("Comienzo del texto\n")

#print(archivo_texto.readlines())

#lista_texto = archivo_texto.readlines() # Guardamos la lista
#lista_texto[1] = "Esta línea ha sido incluida desde el exterior\n"
#archivo_texto.writelines(lista_texto)

#archivo_texto.close()

# FIN ARCHIVOS EXTERNOS