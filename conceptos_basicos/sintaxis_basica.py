# Ejemplo de input por teclado

#num1 = input("Introduce el primer número: ")
#num2 = input("Introduce el segundo número: ")

#if num1 > num2:
#    print("El número 1 es mayor")
#if num1 == num2:
#    print("Son iguales")
#if num1 < num2:
#    print("El número 2 es mayor")



# Imprimir primeros 10 números

#a = 0
#while a <= 10:
#    print(a)
#    a+=1



# Incorrecta, imprime el 11 también

#a = 0
#while a <= 10:
#    a+=1
#    print(a)
    


# Suma de los números pares hasta el 20

#suma = 0
#while a <= 20:
#    suma = suma + a
#    a+=2

#print(suma)



# Suma de los números pares comprendidos entre 100 y 90

#suma = 0
#a = 100
#while a >=90:
#    suma = suma + a
#    a-=2

#print(suma)



# Saldrá "Correcto"

#nombre = "Juan"
#if nombre == "Juan":
#    print("Correcto")
#else:
#    print("Incorrecto")



# Saldrá "Incorrecto"

#nombre = "Juan"
#if nombre == "juan":
#    print("Correcto")
#else:
#    print("Incorrecto")



# Función sin parámetros

#def mensaje():
#    print("Ola")
#    print("Que tal?")
#    print("Adios")

#mensaje()
#mensaje()
#print("Mensaje intermedio")
#mensaje()



# Función con parámetros

#def suma(num1,num2):
#    resultado = num1 + num2
#    return resultado

#print(suma(8,10))

#almacena_resultado = suma(3,2)
#print(almacena_resultado)

#a = 3
#b = 7
#print(suma(a,b))


""" # LISTAS

# Mostrar datos
miLista = ["María","Pepe","Marta","Antonio"]
print(miLista)
print(miLista[0])
print(miLista[2]) # Empieza a contar desde 0
print(miLista[-2]) # Empieza  a contar desde -1 (Antonio)
print(miLista[0:3]) # Imprime los 3 primeros elementos (0 inclusive, 3 exclusive)
print(miLista[:3]) # Python sobreentiende que se empieza en el 0
print(miLista[1:3])
print(miLista[2:]) # Accede desde el elemento con índice 2 hasta el final

print(miLista.index("Antonio")) # Muestra el índice del elemento pasado como parámetro
#print(miLista.index("antonio")) Error, debe ser exactamente igual


# Añadir elementos
miLista.append("Sandra") # Añadir un elemento al final de la lista
print(miLista)
miLista.insert(2, "Javier") # Añadir un elemento en una posición concreta
print(miLista)
miLista.extend(["Pablo","Ana","Lucía"]) # Concatenar listas
print(miLista)
print(miLista.index("Ana"))

# Comprobar si un elemento se encuentra en la lista
print("Pepe" in miLista) # Devuelve "True" o "False", en este caso es True
print("Pepesss" in miLista) # Devuelve False

# Las listas en Python pueden almacenar diferente tipos de datos
miLista2 = ["María", 5, True, 78.35]
miLista2.extend(["Pablo","Ana","Lucía"])
print(miLista2)
print(miLista2[3])
print(miLista2[2])

# Eliminar elementos
miLista.remove("Ana")
print(miLista)
miLista2.remove(5) # Elimina el entero: 5
print(miLista2)
miLista.pop() # Elimina el último elemento de la lista
print(miLista)

# Concatenar listas con el operador "suma"
miLista3 = ["María", 5, True, 78.35]
miLista4 = ["Sandra","Lucía"]
miLista5 = miLista3 + miLista4
print(miLista5)

# Repetir listas con el operador "multiplicación"
miLista3 = miLista3 * 3
print(miLista3)
miLista6 = ["Sara",8] * 5
print(miLista6) """



""" # TUPLAS

miTupla = ("Juan", 13, 1, 1995) # A diferencia de las listas, los elementos de una tupla se escriben entre paréntesis
print(miTupla[0])
print(miTupla[2])

miLista = list(miTupla) # Guardar la tupla en una lista
print(miLista)
print(miTupla)

miLista2 = ["María", 5, True, 78.35] # Guardar la lista en una tupla
miTupla2 = tuple(miLista2)
print(miLista2)
print(miTupla2)

print("María" in miTupla2) # Devuelve "True" o "False", en este caso es True
print(miTupla2.count(78.35)) # Cuenta el número de veces que aparece en la lista, el elemento pasado por parámetro
print(len(miTupla2)) # Nos permite averiguar la longitud de una tupla, cuantos elementos tiene

miTupla3 = ("Juan",) # Crear una tupla unitaria, es decir, de un único elemento. Es necesaria la coma final
print(len(miTupla3))

# Empaquetado de tuplas
miTupla4 = "Juan", 13, 1, 1995 # No es necesario poner los paréntesis al crear una tupla. No muy recomendable
print(miTupla4)

# Desempaquetado de tuplas
miTupla5 = ("Juan", 13, 1, 1995)
nombre, dia, mes, agno = miTupla5
print(nombre)
print(agno)
print(dia)
print(mes)
# Los print no están ordenados para entender que se almacenan los valores correctamente

# EN LAS TUPLAS LOS DATOS SON FIJOS, NO SE PUEDEN AÑADIR NI ELIMINAR """



""" # DICCIONARIOS

# Crear un diccionario
miDiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"} # Los elementos van entre llaves, a diferencia de las listas[] y las tuplas()
print(miDiccionario)
print(miDiccionario["Francia"]) # Muestra el valor asignado a la clave pasada por parámetro, en este caso "Francia"

# Introducir un elemento
miDiccionario["Italia"] = "Lisboa" # Sintaxis: nombre_diccionario[nombre_clave] = valor
print(miDiccionario)

# Modificar un elemento
miDiccionario["Italia"] = "Roma" # Para modificar un dato, basta con sobreescribirlo. Dentro de un diccionario no va haber 2 claves iguales
print(miDiccionario)

# Eliminar un elemento
del miDiccionario["Reino Unido"] # Sintaxis: del nombre_diccionario[nombre_clave]
print(miDiccionario)

# Mezcla de tipos
miDiccionario2 = {"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario2)
print(miDiccionario2[23]) # Si la clave no lleva comillas, al llamarla tampoco las necesita

# Utilizar tuplas
miTupla = ["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario3 = {miTupla[0]:"Madrid",miTupla[1]:"París",miTupla[2]:"Londres",miTupla[3]:"Berlín"}
print(miDiccionario3)
print(miDiccionario3["Francia"])
print(miDiccionario3[miTupla[2]])

miDiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]}
print(miDiccionario4)
print(miDiccionario4["Equipo"])
print(miDiccionario4["Anillos"])

# Diccionario dentro de diccionario
miDiccionario5 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario5)
print(miDiccionario5["Anillos"])

# Métodos interesantes
print(miDiccionario5.keys()) # Muestra las claves que pertenecen al diccionario
print(miDiccionario5.values()) # Muestra los valores
print(len(miDiccionario5)) # Muestra la longitud del diccionario """

# FIN SINTAXIS BÁSICA