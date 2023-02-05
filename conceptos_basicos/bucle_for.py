# BUCLE FOR
# Los bucles FOR recorren listas, tuplas, diccionarios y los caracteres de un string (como mínimo)


""" for i in [1,2,3,456]:
    print("Hola")
    print(i) """
    
    
""" for i in ["Primavera","Verano","Otoño","Invierno"]:
    print("Hola")
    print(i) """
  
    
""" miLista = ["Verano",34,"Juan",34.56,True]
for i in miLista:
    print("Hola")
    print(i) """
    
    
""" for i in ["Primavera","Verano",3]:
    print("Hola", end="") # No hace saltos de línea """


""" for i in ["Primavera","Verano",3]:
    print("Hola", end=" ") # Pone un espacio en blanco """
    
    
""" for i in ["Primavera","Verano",3]:
    print("Hola", end="quetal") """
 
 
""" # Imprime la palabra "Hola", el mismo número de veces que caracteres en el string    
for i in "juan@pildorasinformaticas.es":
    print("Hola", end="")"""


""" # Comprobar si se trata de un correo electrónico (debe contener el caracter: @)
email = False
for i in "juan@pildorasinformaticas.es":
    
    if (i=="@"):
        email = True
    
if email == True:
    print("Email es correcto")
     
else:
    print("Email no es correcto") """
    
    
""" # Comprobar cualquier dirección de Email
email = False
miEmail = input("Introduce tu dirección de Email: ")

for i in miEmail:
    
    if (i=="@"):
        email = True
    
if email == True:
    print("Email es correcto")
     
else:
    print("Email no es correcto") """
    
    
""" # Comprobar si se trata de un correo electrónico (debe contener el caracter: @ y un punto)
contador = 0
miEmail = input("Introduce tu dirección de Email: ")

for i in miEmail:
    
    if (i=="@" or i=="."):
        contador = contador + 1
    
if contador == 2:
    print("Email es correcto")
     
else:
    print("Email no es correcto") """
    
    
""" for i in range(5):
    print("Hola") # Lo muestra 5 veces
    print(i) # Empieza a contar en el 0, es decir, tendrá los valores: 0 1 2 3 4 """
    

""" for i in range(5):
    print(f"valor de la variable {i}") # Notación especial para concatenar texto con variables """


""" for i in range(5,10):
    print(f"valor de la variable {i}") """
    

""" for i in range(5,49,3): # El tercer parámetro indica el intervalo: 5 8 11 14 ...
    print(f"valor de la variable {i}") """
    

""" # Comprobar si es un email con el método range()
valido = False
email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@": # Revisión de listas: buscar un objeto en una lista
        valido = True
        
if valido:
    print("Email correcto")
else:
    print("Email incorrecto") """

# FIN BUCLE FOR