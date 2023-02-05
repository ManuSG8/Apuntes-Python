# POO I

# Construir una clase (el nombre de la clas debe empezar por mayúscula)

class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    
# Establecer un comportamiento (los comportamientos se establecen mediante métodos y deben estar dentro del método class)

    def arrancar(self):
        self.enmarcha = True
    
    
    def parar(self):
        self.enmarcha = False
    
    
    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    
    
miCoche = Coche() # Crear un objeto / Instanciar una clase / Ejemplarizar una clase


# Ver las propiedades del objeto

print(f"El largo del coche es {miCoche.largoChasis}")
print(f"El coche tiene {miCoche.ruedas} ruedas")

miCoche.arrancar()
print(miCoche.estado())

miCoche.parar()
print(miCoche.estado())


# RESUMEN: la clase "Coche" tiene 4 propiedades (largoChasis, anchoChasis, ruedas, enmarcha) y 3 comportamientos (arrancar(), parar(), estado())

# FIN POO I