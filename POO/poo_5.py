# POO V

# Polimorfismo

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")
        

class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")
        
        
class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")
        
        
#miVehiculo = Moto()
#miVehiculo.desplazamiento()

#miVehiculo2 = Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3 = Camion()
#miVehiculo3.desplazamiento()


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)

miVehiculo = Moto()
desplazamientoVehiculo(miVehiculo)

miVehiculo = Coche()
desplazamientoVehiculo(miVehiculo)

# FIN POO V