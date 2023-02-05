# GUARDADO PERMANENTE


# Queremos crear personas, y almacenarlas en un fichero externo

import pickle

class Persona():
    
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ",self.nombre)
        
    def __str__(self): # Convierte a cadena de texto la información de un objeto
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    

class ListaPersonas():
   
    personas = []
    
    def __init__(self):
        listaDePersonas = open(r"C:\Users\Manuel\Desktop\Python\ficheroPersonas", "ab+") # ab+, agregar información binaria
        listaDePersonas.seek(0) # Debemos desplazar el cursor al principio, para poder leerlo más adelante, sino estaría al final

        try: # Usamos un try porque la primera vez que accedemos a la lista, estará vacía y nos dará error
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas))) # Este método len nos devuelve cuantas persona hay en esa lista
        except:
            print("El fichero está vacío")
        finally: # Empleamos el método finally porque se ejecutará siempre y así podemos cerrarla y eliminarla de memoria como hacemos habitualmente
            listaDePersonas.close()
            del(listaDePersonas)
        
    def agregarPersonas(self, p):
       self.personas.append(p)
       self.guardarPesonasEnFicheroExterno()
       
    def mostrarPersonas(self):
        for p in self.personas:
            print(p) # Prueba print(p.nombre) por ejemplo
            
    def guardarPesonasEnFicheroExterno(self):
        listaDePersonas = open(r"C:\Users\Manuel\Desktop\Python\ficheroPersonas", "wb") # Escribir información binaria (wb)
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
        
    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)
            
            
miLista = ListaPersonas()
    
    
persona = Persona("Sandra","Femenino", 29)

miLista.agregarPersonas(persona)

miLista.mostrarInfoFicheroExterno()


persona = Persona("Antonio","Masculino", 39)

miLista.agregarPersonas(persona)

miLista.mostrarInfoFicheroExterno()

#p = Persona("Ana","Femenino", 19)

#miLista.agregarPersonas(p)


#miLista.mostrarPersonas()