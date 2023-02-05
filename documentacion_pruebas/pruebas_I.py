# PRUEBAS I


import doctest # Hay que importar la librería

#def areaTriangulo(base, altura):

#    """
#    Calcula el área de un triángulo

#    >>> areaTriangulo(3,6)
#    9.0
    
#    """

#    return (base*altura)/2


#doctest.testmod() # Para hacer las pruebas



# ¿Que pasa si la función devuelve un string?

#def areaTriangulo(base, altura):

#    """
#    Calcula el área de un triángulo

#    >>> areaTriangulo(3,6)
#    'El área del triángulo es: 9.0'
    
#    """
#    return "El área del triángulo es: " + str((base*altura)/2)


#doctest.testmod()

# CUIDADO: en Python los string llevan comillas simples por defecto. Fíjate bien como hay que ponerlo en la parte del test



# Múltiples test

def areaTriangulo(base, altura):

    """
    Calcula el área de un triángulo

    >>> areaTriangulo(3,6)
    8.0

    >>> areaTriangulo(4,5)
    10.0

    >>> areaTriangulo(9,3)
    13.5
    
    """

    return (base*altura)/2


doctest.testmod()