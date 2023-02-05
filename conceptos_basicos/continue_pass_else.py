# INSTRUCCIONES CONTINUE - PASS - ELSE

# CONTINUE. Ignora el resto del bucle y pasa a la siguiente iteración

""" for letra in "Python":
    
    if letra == "h":
        continue
    
    print(f"Viendo la letra: {letra}") """
    

""" nombre = "Pildoras Informaticas" 
print(f"Número de caracteres {len(nombre)}") # Cuenta el espacio en blanco

# Sólo queremos saber el número de letras

contador = 0
for i in nombre:
    
    if i==" ":
        continue
    
    contador+=1
    
print(f"Número de letras: {contador}") """



# PASS. Devuelve un null. Es como si el bucle no se ejecutase. Se suele utilizar para dejar el trabajo a medias o para hacer más tarde

""" class MiClase:
    pass # Para implementar más tarde """
    


# ELSE.  

""" email = input("Intoduce tu email: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False
    
print(arroba) """

# FIN CONTINUE - PASS - ELSE