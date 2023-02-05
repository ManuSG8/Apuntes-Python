# No puede haber herencia, si no no funciona

class Coche():
    
    def __init__(self, marca):
        
        self.__marca = marca
        self.__ruedas = 4
        
    def estado(self):
        print(f"El {self.__marca} tiene {self.__ruedas} ruedas")
        
        
miCoche = Coche("Renault")

miCoche.estado()

miCoche.__marca = "Citroen"

miCoche.__ruedas = 3

miCoche.estado()        