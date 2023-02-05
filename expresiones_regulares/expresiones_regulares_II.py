# EXPRESIONES REGULARES II


import re

"""lista_nombres = ["http://pildorasinformaticas.es",
                    "ftp://pildorasinformaticas.es",
                    "http://pildorasinformaticas.com",
                    "ftp://pildorasinformaticas.com",
                    "http://informaticaenespaña.es",
                    "María Martín",
                    "Sandra López",
                    "Santiago Martín",
                    "Sandra Fernández"]

for nombre in lista_nombres:
    if re.findall("^Sandra", nombre): # ^ Significa que empieza por...
        print(nombre)

for nombre in lista_nombres:
    if re.findall("Martín$", nombre): # $ Significa que termina por...
        print(nombre)

for nombre in lista_nombres:
    if re.findall(".es$", nombre): 
        print(nombre)

for nombre in lista_nombres:
    if re.findall("[ñ]", nombre): 
        print(nombre)"""


lista_nombres = ["hombres",
                    "mujeres",
                    "niños",
                    "niñas",
                    "mascotas",
                    "camión",
                    "camion"]

for nombre in lista_nombres:
    if re.findall("niñ[oa]s", nombre): 
        print(nombre)

for nombre in lista_nombres:
    if re.findall("cami[oó]n", nombre): 
        print(nombre)