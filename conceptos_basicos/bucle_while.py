# BUCLE WHILE

""" i = 1
while i <= 10:
    print(f"Ejecución {i}")
    i+=1 """
    

""" # Comprobar que la edad no sea negativa

edad = int(input("Introduce tu edad: "))
while edad < 0:
    print("Has introducido una edad negativa. Vuelve a intentarlo.")
    edad = int(input("Introduce tu edad: "))
    
print("Gracias por colaborar. Puedes pasar")
print(f"Edad del aspirante: {edad}") """
 

""" # Y que no sea mayor de 100

edad = int(input("Introduce tu edad: "))
while edad < 0 or edad > 100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo.")
    edad = int(input("Introduce tu edad: "))
    
print("Gracias por colaborar. Puedes pasar")
print(f"Edad del aspirante: {edad}") """


""" # Como evitar que un bucle sea infinito por mucho que se empeñe el usuario

import math
print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce un número: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")
    
    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado.")
        break 
    
    numero = int(input("Introduce un número: "))
    if numero < 0:
        intentos+=1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {solucion}") """


""" # Otra posible solución del ejercicio anterior    
import math
print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce un número: "))

intentos = 0

while numero < 0 and intentos < 2:
    print("No se puede hallar la raíz de un número negativo")
    
    numero = int(input("Introduce un número: "))
    intentos+=1
    
if intentos <= 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {solucion}")
else:
    print("Has consumido demasiados intentos") """
    
# FIN BUCLE WHILE