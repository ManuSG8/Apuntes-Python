class Coche():
    
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.ruedas = 4
        self.velocidad = 0
        self.enmarcha = False
        self.parado = True
        self.acelerando = False
        self.frenando = False
        
    def acelerar(self, velocidad):
        
        if(velocidad > 0):
            self.velocidad = velocidad
            self.enmarcha = True
            self.parado = False
            self.acelerando = True
            self.frenando = False
            print(f"El coche {self.marca} {self.modelo} está acelerando y va a una velocidad de {self.velocidad} km/h")
        
        elif(velocidad == 0):
            self.velocidad = 0
            self.enmarcha = False
            self.parado = True
            self.acelerando = False
            self.frenando = False
            print(f"El coche {self.marca} {self.modelo} está parado y va a una velocidad de {self.velocidad} km/h")
        
        elif(velocidad < 0):
            print("Velocidad errónea")
        
    def frenar(self, velocidad):
        
        if(velocidad > 0):
            self.velocidad = velocidad
            self.enmarcha = True
            self.parado = False
            self.acelerando = False
            self.frenando = True
            print(f"El coche {self.marca} {self.modelo} está frenando y va a una velocidad de {self.velocidad} km/h")
        
        elif(velocidad == 0):
            self.velocidad = 0
            self.enmarcha = False
            self.parado = True
            self.acelerando = False
            self.frenando = False
            print(f"El coche {self.marca} {self.modelo} está parado y va a una velocidad de {self.velocidad} km/h")
        
        elif(velocidad < 0):
            print("Velocidad errónea")
            
    def pincharRueda(self, num_ruedas):
        
        self.ruedas = self.ruedas - num_ruedas
        print(f"El coche tiene {self.ruedas} ruedas en buen estado")
        
    def cambiarRuedas(self, num_ruedas):
        
        self.ruedas = self.ruedas + num_ruedas
        print(f"El coche tiene {self.ruedas} ruedas en buen estado")
        
           
class CocheElectrico(Coche):
    
    def __init__(self, autonomia, marca, modelo):
        
        super().__init__(marca, modelo)
        self.autonomia = autonomia
        self.cargado = False
        self.cargando = False
        self.descargado = True
        self.descargando = False # Implementa esto, que ahora estou cansado pff
        
             
miCoche = Coche("Renault", "Megane")

    
miCoche.acelerar(60)

miCoche.acelerar(0)

miCoche.acelerar(-40)


#miCoche.frenar(40)

#miCoche.frenar(0)

#miCoche.frenar(-40)


#miCoche.pincharRueda(2)

#miCoche.cambiarRuedas(1)

#print(miCoche.ruedas)