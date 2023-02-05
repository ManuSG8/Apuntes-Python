# EXCEPCIONES
# Son errores que ocurren durante la ejecución del programa. La sintaxis del código es correcta pero durante la ejecución ha ocurrido "algo inesperado"



""" # Ejemplo de error durante la ejecución de un programa

def suma(num1, num2):
    	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	return num1/num2
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")

# Imaginemos que el programa continúa a partir de aqui...

# El usuario podría intentar dividir 8/0, lo cual daría un error en el programa porque no se puede dividir entre 0. Y jamás se seguiría ejecutando el programa """



""" # Solución: captura o control de excepción (decirle al código que intente realizar la operación, y en caso de que no pueda, que siga ejecutando el resto del programa)

def suma(num1, num2):
    	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:		
	    return num1/num2
    except ZeroDivisionError: # Nombre/identificador del error
        print("No se puede dividir entre 0")
        return "Operación errónea"
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")

# Imaginemos que el programa continúa a partir de aqui... """



""" # Otro error: el usuario podría introducir algo diferente a un número entero (str,double,boolean,...)

def suma(num1, num2):
    	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:		
	    return num1/num2
    except ZeroDivisionError: # Nombre/identificador del error
        print("No se puede dividir entre 0")
        return "Operación errónea"
	
while True: # Bucle infinito
    try:
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))
        break # Si las dos líneas anteriores se ejecutan correctamente, leerá el break y se salirá del bucle while. Si no, saltará al except y volverá al bucle infinito	
    except ValueError:
        print("Los valores introducidos no son correctos. Inténtalo de nuevo")

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecución del programa ")

# Imaginemos que el programa continúa a partir de aqui... """



""" # Capturar excepciones en bloque

def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print(f"La división es: {op1/op2}")
        
    except ValueError:
        print("El valor introducido es erróneo")
        divide()
         
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        divide()
        
    print("Cálculo finalizado") # Fuera del bloque try, pero podría estar dentro
    
divide() """



""" # Error general

def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print(f"La división es: {op1/op2}")
        
    except :
        print("Ha ocurrido un error")
          
    print("Cálculo finalizado")
    
divide() """



""" # Cláusula "finally"

def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print(f"La división es: {op1/op2}")
        
    except ValueError:
        print("El valor introducido es erróneo")
         
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    
    finally: # No es obligatorio, pero en algunos casos es recondable. Siempre se ejecutará lo que está dentro del finally, sí o sí
        print("Cálculo finalizado")
    
divide() """



""" # De este modo no capturaría el error, pero ejecutaría el finally

def divide():
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print(f"La división es: {op1/op2}")
    
    finally:
        print("Cálculo finalizado")
    
divide() """



""" # Lanzar excepciones (nosotros lanzaremos excepciones de forma intencionada)

# En este programa no tiene sentido que evalue una edad negativa

def evaluaEdad(edad):
    
    if edad < 0:
        raise TypeError("No se permiten edades negativas") # El nombre del error lo eliges tu (puedes crear una clase para crear tu propio error). Mensaje personalizado entre parentesis y comillas
    
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuídate..."
    
print(evaluaEdad(70))
print(evaluaEdad(35))
print(evaluaEdad(-23)) """



""" # Otro ejemplo

# No se puede calcular la raíz cuadrada de un número negativo

import math

def calculaRaiz(num1):
    
    if num1 < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
    
op1 = int(input("Introduce un número: "))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo: # Le damos un alias al error
    print(ErrorDeNumeroNegativo)
    
print("Programa finalizado") """