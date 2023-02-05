# DECORADORES I
# Funciones que a su vez añaden funcionalidades a otras funciones
# Estructura: formado por 3 funciones (A, B , C) donde A recibe como parámetro a B para devolver C. Un decorador devuelve una función
# def función_decorador(función):
#   def función_interna():
#       código de la función interna
#   return función_interna


def funcion_decoradora(funcion_parametro):

    def funcion_interior():
        
        print("Vamos a realizar un cálculo: ")

        funcion_parametro() # Para que ejecute el código de la función correspondiente

        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)

suma()
print("")
resta()