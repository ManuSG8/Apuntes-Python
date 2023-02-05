# EXPRESIONES REGULARES IV
# La función "match" busca si hay coincidencia al inicio de una cadena de texto. Siempre al inicio


import re

"""nombre1 = "Sandra López"

nombre2 = "Antonio Gómez"

nombre3 = "sandra López"

nombre4 = "Jara Pérez"

nombre5 = "Lara Martínez"

cadena1 = "Laura Pérez"

cadena2 = "7578937485893"

cadena3 = "a789789898"

if re.match("Sandra", nombre1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

if re.match("Sandra", nombre3, re.IGNORECASE): # Ignora las minúsculas y mayúsculas
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

if re.match(".ara", nombre4): # Pruebe con nombre4 y nombre5
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

if re.match("\d", cadena2): # Busca si empieza por un dígito. Prueba con cadena1, cadena2, cadena3
    print("Hemos encontrado el número")
else:
    print("No lo hemos encontrado")"""


# La función "search" busca en toda la cadena de texto

"""nombre1 = "Jara López"

nombre2 = "Antonio Gómez"

nombre3 = "Lara López"

if re.search("López", nombre2): # También admitiría el tercer parámetro, igual que el "match"
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")"""


# Otros ejemplos útiles
codigo1 = "ajlksdjfklaklsdjfkljsdkl fkljsadklfjkljsdfkljlañkjdlfja71klajkldjsfjaklsdfjklajsfjkla sdfklaklsdfjlkajksdf"

codigo2 = "asjfljkljsdfjs71klajskldj fkljaskldfjklasdklfjkl asdfjkljakls dfjklajsdlñfjkldsfjklajslkjl"

codigo3 = "kajkldsjfkl jdklsfjkljeio a jdlfjioeujkkljadsf"

if re.search("71", codigo1):
    print("Hemos encontrado el número")
else:
    print("No lo hemos encontrado")


var = "71"

if re.search(var, codigo3):
    print("Hemos encontrado el número")
else:
    print("No lo hemos encontrado")