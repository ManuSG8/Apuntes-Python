# FUNCIÓN FILTER
# Verifican que los elementos de una secuencia cumplen una condición,
# devolviendo  un iterador con los elementos que cumplen dicha condición


# Detectar los número pares en una lista
"""def numero_par(num):

    if num % 2 == 0:
        return True

numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(numero_par, numeros))) # Con list nos devuelve el objeto en formato lista"""


# Combinado con las funciones lambda
"""numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(lambda numero: numero%2==0, numeros)))"""


# Filtrar objetos (más usado)
class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    
    def __str__(self):
        return "{} que trabaja como {} y tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Presidenta", 85000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria", 27000),
    Empleado("Mario", "Botones", 21000),
]

salarios_altos = filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado in salarios_altos:
    print(empleado)