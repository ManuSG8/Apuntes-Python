# POO III


# Encapsulación de métodos (haces que un método sólo sea accesible desde dentro de la clase)

class Coche():
    
    
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 
        self.__enmarcha = False
    
    
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo. No se puede arrancar"
        else:
            return "El coche está parado"
        
        
    def parar(self):
        self.__enmarcha = False
    
    
    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}")
        
        
    # Vamos a añadir la funcionalidad de chequear que todo esté correcto antes de arrancar
    def __chequeo_interno(self): # Se encapsula con 2 guiones bajos. Ojo: después hay que escribirlos en el resto de la clase también con los 2 guiones bajos
        print("Realizando chequeo interno")
        
        # No lo complicamos, y directamente las inicializamos a OK en vez de pasar su estado por parámetro
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "CERRADAS"
        
        if(self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "CERRADAS"):
            return True
        else:
            return False
        
    
miCoche = Coche()

print(miCoche.arrancar(True)) 

miCoche.estado()


print("------------------- A continuación creamos el segundo objeto -------------------")


miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()

#print(miCoche2.__chequeo_interno) # No nos deja acceder al método encapsulado

# FIN POO III