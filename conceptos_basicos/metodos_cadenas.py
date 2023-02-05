# MÉTODOS DE CADENAS

# upper() Convierte a mayúsculas.
# lower() Convierte a minúsculas.
# capitalize() Pone la primera letra en mayúscula.
# count() Cuenta las veces que aparece un caracter o una cadena de caracteres dentro de un texto.
# find() Representa el índice donde se encuentra el caracter o cadena de caracteres dentro de un texto.
# isdigit() Devuelve un boolean. Nos dice si el valor introducido es un dígito o no lo es.
# isalnum() Compruebe si son alfanumericos.
# isalpha() Comprueba si hai solo letras, los espacios no cuentan.
# split() Separa por palabras utilizando espacios.
# strip() Elimina los espacios en blanco sobrantes al principio y al final.
# replace() Cambia una letra o palabra por otra.
# rfind() Hace lo mismo que le find(), pero contando desde atrás.

# http://pyspanishdoc.sourceforge.net/lib/string-methods.html Aquí están todos.


# Ejemplos sencillos

""" nombreUsuario = input("Introduce tu nombre: ")

print("El nombre es: ",nombreUsuario)
print("El nombre es: ",nombreUsuario.upper())
print("El nombre es: ",nombreUsuario.lower())
print("El nombre es: ",nombreUsuario.capitalize()) """


""" edad = input("Introduce tu edad: ")
#print(edad.isdigit())

while(edad.isdigit() == False):
    
    print("Por favor introduce un valor númerico")
    edad = input("Introduce tu edad: ")


if (int(edad) < 18): # Recordatorio: todo lo que se introduce a través del input, se almacena como texto
    
    print("No puedes pasar")

else:
    
    print("Puedes pasar") """



#Crea un programa que pida introducir una dirección de email por teclado. El programa 
#debe imprimir en consola si la dirección de email es correcta o no en función de si esta 
#tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o 
#ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email 
#o al final, la dirección también será errónea

mailUsuario = input("Introduce tu dirección de email: ")

arroba = mailUsuario.count("@")

if (arroba != 1 or mailUsuario.rfind("@") == (len(mailUsuario)-1) or mailUsuario.find("@") == 0):
    
    print("Mail incorrecto")
    
else:
    print("Mail correcto")
    
# FIN MÉTODOS DE CADENAS