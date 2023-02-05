# DECORADORES II


# Si las funcións básicas reciben parámetros debemos indicárselo a la función decoradora en la función interior y en la llamada a la función parámetro
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs): # Con *args le indicamos que puede recibir un número indeterminado de parámetros. Con **kwargs ver línea 33
        
        print("Vamos a realizar un cálculo: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base, exponenente):
    print(pow(base,exponenente))

suma(7,5,9)
print("")
resta(12,10)
print("")
potencia(base=5, exponente=3) # Para ponerlo así (clave=valor), debemos poner el **kwargs que significa que puede recibir argumentos de tipo clave=valor