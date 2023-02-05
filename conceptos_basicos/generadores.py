# GENERADORES
# Son estructuras que extraen valores de una función y se almacenan en objetos iterables (que se pueden recorrer)
# Se almacenan de uno en uno
# Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente ("Suspensión de estado")
# Ventajas: Más eficientes que una función tradicional. Muy útiles con listas de valores infinitos.
# Sintaxis: Función tradicional - return variable     Generador - yield variable (adicionalmente, un generador también puede llevar un return variable)


""" # Función tradicional

def generaPares(limite):
    num = 1
    miLista = []  
    while num <= limite:
        miLista.append(num * 2)
        num+=1
        
    return miLista

print(generaPares(10)) """



""" # Generador

def generaPares(limite):
    num = 1
    while num <= limite:
        yield num * 2
        num+=1
        
devuelvePares = generaPares(10) # Almacenamos el objeto iterable que devuelve la función en una variable

for i in devuelvePares: # Recorremos el objeto iterable con un bucle (for o while)
    print(i) """



""" # Recorrer el objeto iterable

def generaPares(limite):
    num = 1
    while num <= limite:
        yield num * 2
        num+=1
        
devuelvePares = generaPares(10)
   
print(next(devuelvePares)) # Devuelve el primer valor almacenado

print("Aquí podría ir más código...")

print(next(devuelvePares)) # Y el siguiente...

print("Aquí podría ir más código...")

print(next(devuelvePares)) # Y el siguiente...

print("Aquí podría ir más código...")

print(next(devuelvePares)) # Y el siguiente... """



""" # Yield from - Utilidad: simplificar el código de los generadores en el caso de utilizar bucles anidados

def devuelveCiudades(*ciudades): # El asterisco significa que la función puede recibir un número INDETERMINADO de elementos y en forma de tupla
    for elemento in ciudades:
        yield elemento
        
ciudades_devueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas)) # Estas dos últimas líneas devuelven los 2 primeros elementos """



""" # Por ejemplo, Madrid: el elemento es la palabra "Madrid" que está formada por los subelementos que son las letras "M" "a" "d" "r" "i" "d"

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento
        
ciudades_devueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas)) """



""" # Simplificar el código anterior con "yield from"

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield from elemento
        
ciudades_devueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas)) """

# FIN GENERADORES