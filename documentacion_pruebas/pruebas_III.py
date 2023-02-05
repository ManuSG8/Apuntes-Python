# PRUEBAS III


import math
import doctest

def raizCuadrada(listaNumeros):

    """
    La función devuelve una lista con la 
    raíz cuadrada de los elementos númericos
    pasados por parámetros en otra lista

    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista = []
    >>> for i in [4, -9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error

    """

    return [math.sqrt(n) for n in listaNumeros]


#print(raizCuadrada([9,16,25,36]))

doctest.testmod()

# Con los 3 puntos, anidas las líneas de código. Nos hemos complicado un poco al crear la lista, para enseñarnos esto

# Los 3 puntos en la línea 25 indica que puede ir cualquiera cosa entre esas dos líneas