# Comprobar si un número pasado por parámetro es un cuadrado

import math
def is_square(n):  
    try:
        num = math.sqrt(n)
        if(int(n**0.5)**2 == int(n)):
            return True
        else: 
            return False
    except:
        return False



# Otras soluciones

import math

def is_square(n):    

    if n < 0:
        return False

    sqrt = math.sqrt(n)
    
    return sqrt.is_integer()



import math
def is_square(n):    
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False