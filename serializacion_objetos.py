# SERIALIZACIÓN DE OBJETOS

import pickle

class Vehiculo():
    
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        
    def arrancar(self):
        self.enmarcha = True
        
    def acelerar(self):
        self.acelera = True
        
    def frenar(self):
        self.frena = True
        
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)
        
        
coche1 = Vehiculo("Mazda","MX5")
coche2 = Vehiculo("Seat","Leon")
coche3 = Vehiculo("Renault","Megane")

coches = [coche1, coche2, coche3] # Colección de objetos

fichero = open(r"C:\Users\Manuel\Desktop\Python\lisCoches","wb")

pickle.dump(coches, fichero) # Volcamos la coleccion "coches" en el fichero "fichero" que es "lisCoches"

fichero.close()

del (fichero)


# Vamos a rescatar el fichero y leer la información que hay en su interior

ficheroApertura = open(r"C:\Users\Manuel\Desktop\Python\lisCoches","rb")

misCoches = pickle.load(ficheroApertura)

print(misCoches)

ficheroApertura.close()

for i in misCoches:
    
    i.estado()