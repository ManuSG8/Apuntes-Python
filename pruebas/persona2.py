class Persona():
    
    def __init__(self, nombre, edad, altura, peso):
        
        self.__nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.despierta = True
        self.duerme = False
        self.camina = False
        self.parado = True
    
    def despertar(self):
        self.despierta = True
        self.duerme = False
        return "La persona está despierta"
        
    def dormir(self):
        self.despierta = False
        self.duerme = True
        self.parar() # Si está dormido no puede caminar, a menos que sea sonámbulo jajaja
        print("La persona duerme")
        
    def caminar(self):
        self.camina = True
        self.parado = False
        
    def parar(self):
        self.camina = False
        self.parado = True
    
    def incrementarEdad(self, incremento):
        self.edad = self.edad + incremento
        
    def crecerAltura(self, inc_altura):
        if inc_altura >= 0:
            self.altura = self.altura + inc_altura
        elif inc_altura < 0:
            print("No se pudo realizar el incremento de altura. Debe ser un número positivo")
        
    #def estado(self):
    #print(f"La persona está despierta: {self.despierta}") # Equivalente: print("{}".format(self.despierta))
    
    def estado(self):
        if self.camina:
            print(f"{self.__nombre} está caminando, tiene {self.edad} años y mide {self.altura} cm")
        else:
            print(f"{self.__nombre} está parado, tiene {self.edad} años y mide {self.altura} cm")
            
            
persona = Persona("Juan", 15, 174, 68)

persona.estado()

persona.__nombre="Jose"

persona.estado()