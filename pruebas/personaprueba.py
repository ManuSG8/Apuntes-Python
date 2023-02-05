class Persona():
    
    def __init__(self, nombre, edad):
        
        self.setNombre(nombre)
        self.setEdad(edad)
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setEdad(self, edad):
        self.__edad = edad
        
    def getEdad(self):
        return self.__edad
    
    def estado(self):
        print("El nombre es: ",self.__nombre,"\nLa edad es: ",self.__edad)
        

p = Persona("Juan", 24)

p.estado()

p.setNombre("Sara")

print("Hola ",p.getNombre())

p.estado()