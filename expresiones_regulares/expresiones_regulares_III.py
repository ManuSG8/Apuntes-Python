# EXPRESIONES REGULARES III


import re

"""lista_nombres = ["Ana",
                    "Pedro",
                    "María",
                    "Rosa",
                    "Sandra",
                    "Celia"]

for nombre in lista_nombres:
    if re.findall("[o-t]", nombre): # Devuelve los nombres que tienen letras entre la o y la t en su nombre
        print(nombre)
print("\n")
for nombre in lista_nombres:
    if re.findall("^[O-T]", nombre): # Devuelve los nombres que empiecen por letras entre la o y la t 
        print(nombre)"""


"""lista_nombres = ["Ma1",
                    "Se1",
                    "Ma2",
                    "Ba1",
                    "Ma3",
                    "Va1",
                    "Va2",
                    "Ma4",
                    "MaA",
                    "Ma5",
                    "MaB",
                    "MaC"]

for nombre in lista_nombres:
    if re.findall("Ma[0-3]", nombre):
        print(nombre)
print("\n")
for nombre in lista_nombres:
    if re.findall("Ma[^0-3]", nombre): # Negación del rango
        print(nombre)
print("\n")
for nombre in lista_nombres:
    if re.findall("Ma[0-3A-B]", nombre):
        print(nombre)"""


lista_nombres = ["Ma.1",
                    "Se1",
                    "Ma2",
                    "Ba1",
                    "Ma:3",
                    "Va1",
                    "Va2",
                    "Ma4",
                    "MaA",
                    "Ma.5",
                    "MaB",
                    "Ma:C"]

for nombre in lista_nombres:
    if re.findall("Ma[.:]", nombre):
        print(nombre)