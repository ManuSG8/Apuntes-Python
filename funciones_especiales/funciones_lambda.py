# FUNCIONES LAMBDA
# Las funciones complejas (con bucles, condicionales, etc.) no se pueden resumir o transformar en funciones lambda. Sólo puede devolvernos un cálculo


# Permite simplificar la sintaxis de este tipo de funciones
"""def area_triangulo(base, altura):

    return (base*altura)/2

triangulo1 = area_triangulo(5,7)

triangulo2 = area_triangulo(9,6)

print(triangulo1)

print(triangulo2)"""


# Funcion lambda
"""area_triangulo = lambda base, altura:(base*altura)/2 # Los 2 puntos es como escribir el return

print(area_triangulo(7,5))

triangulo1 = area_triangulo(9,6)
print(triangulo1)"""


# Otro ejemplo
"""al_cubo = lambda numero:pow(numero, 3) # Tambien vale: numero**3

print(al_cubo(15))

cubo1 = al_cubo(20)
print(cubo1)"""


# Otro ejemplo (dar formato)
destacar_valor = lambda comision:"¡{}! €".format(comision)

comision_Ana = 15585

print(destacar_valor(comision_Ana))