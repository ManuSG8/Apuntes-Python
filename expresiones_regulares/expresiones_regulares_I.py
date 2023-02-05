# EXPRESIONES REGULARES I
# Son una secuencia de caracteres que forman un patrón de búsqueda
# Usos: buscar un texto que se ajuste a un formato determinado (correo electrónico), buscar si existe o no una cadena de caracteres dentro de un texto,
# contar el número de coincidencias dentro de un texto, etc.


import re

cadena = "Vamos a aprender expersiones regulares en Python. Python es un lenguaje de sintaxis sencilla"



#print(re.search("aprender", cadena)) # Averiguar si una cadena de caracteres se encuentra en un texto. Devuelve un objeto o "None" si no hay



"""textoBuscar = "aprender"

if re.search(textoBuscar, cadena) is not None:

    print("He encontrado el texto")

else:

    print("No he encontrado el texto")"""



"""textoBuscar = "aprender"

textoEncontrado = re.search(textoBuscar, cadena)

print(textoEncontrado.start()) # Nos dice el número de carácter donde empieza la cadena dentro del texto

print(textoEncontrado.end()) # Nos dice el número de carácter donde finaliza la cadena dentro del texto

print(textoEncontrado.span()) # Combina las dos anteriores y los devuelve en una tupla"""



textoBuscar = "Python"

print(re.findall(textoBuscar, cadena)) # Nos devuelve una lista con la cadena a buscar repetida todas las veces que aparece

print(len(re.findall(textoBuscar, cadena))) # Nos devuelve el número de veces que aparece la cadena a buscar en el texto