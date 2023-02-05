# POO II


""" class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        
        if(self.enmarcha): # Si no se pone nada se entiende como: self.enmarcha == True
            return "El coche está en marcha"
        else:
            return "El coche está parado"
        
    
    def parar(self):
        self.enmarcha = False
    
    def estado(self):
        print(f"El coche tiene {self.ruedas} ruedas, un ancho de {self.anchoChasis} y un largo de {self.largoChasis}")
        
    
miCoche = Coche() # Crear un objeto / Instanciar una clase / Ejemplarizar una clase

print(f"El largo del coche es {miCoche.largoChasis}")
print(f"El coche tiene {miCoche.ruedas} ruedas")

print(miCoche.arrancar(True)) # Debemos pasar True o False porque enmarcha es un boolean

miCoche.estado()


print("------------------- A continuación creamos el segundo objeto -------------------")


miCoche2 = Coche() # Evidentemente no puede haber 2 objetos con el mismo nombre

print(f"El largo del coche es {miCoche2.largoChasis}")
print(f"El coche tiene {miCoche2.ruedas} ruedas")

print(miCoche2.arrancar(False))

miCoche2.estado() """


""" class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
Esto es el estado inicial de los objetos, para especificar que van a formar parte del estado inicial de los objetos usamos el método constructor """

""" class Coche():
    
    # CONSTRUCTOR
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # Con 2 guiones bajos antes de la variable, la encapsulamos. Ojo: después hay que escribirlos en el resto de la clase también con los 2 guiones bajos
        self.__enmarcha = False
    
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
        
    
    def parar(self):
        self.__enmarcha = False
    
    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}")
        
    
miCoche = Coche()

print(miCoche.arrancar(True)) 

miCoche.estado()


print("------------------- A continuación creamos el segundo objeto -------------------")


miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.ruedas = 3 # Esto no debería permitirse. Para ello empleamos la encapsulación de variables

miCoche2.estado() """

# FIN POO II