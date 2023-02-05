from random import randint
from random import choice

def juego():

    num = randint(0,10)

    num2 = randint(0,10)

    print(num, " + ", num2)

    print("")

    resultado = int(input())

    if (num + num2) == resultado:

        print("Correcto")

    else:

        print("Incorrecto")


juego()


"""def juego():

    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    num1 = choice(lista)

    num2 = choice(lista)

    print(num1, " + ", num2)

    resultado = int(input())

    if (num1 + num2) == resultado:

         print("Correcto")

    else:

        print("Incorrecto")


juego()"""