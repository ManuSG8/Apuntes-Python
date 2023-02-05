class Persona():
    
    def __init__(self, nombre, edad, altura, peso):
        
        self.nombre = nombre
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
            print(f"{self.nombre} está caminando, tiene {self.edad} años y mide {self.altura} cm")
        else:
            print(f"{self.nombre} está parado, tiene {self.edad} años y mide {self.altura} cm")
        
          
class Empleado(Persona):
    
    def __init__(self, salario, tipoContrato, nombre, edad, altura, peso):
        super().__init__(nombre, edad, altura, peso)
        
        self.salario = salario
        self.tipoContrato = tipoContrato
    
    def incrementarSalario(self, plus):
        if(self.salario+plus < 1000):
            print("No puede tener un salario inferior al SMI")
        else:
            self.salario = self.salario + plus
    
    def estado(self): # Sobreescritura de métodos 
        if self.camina:
            print(f"{self.nombre} está caminando, tiene {self.edad} años, mide {self.altura} cm, su contrato es {self.tipoContrato} y su sueldo es de {self.salario} euros")
        else:
            print(f"{self.nombre} está parado, tiene {self.edad} años, mide {self.altura} cm, su contrato es {self.tipoContrato} y su sueldo es de {self.salario} euros")
            
            
class Peon(Empleado):
    def __init__(self, puestoTrabajo, salario, tipoContrato, nombre, edad, altura, peso):
        super().__init__(salario, tipoContrato, nombre, edad, altura, peso)
        
        self.puestoTrabajo = puestoTrabajo
        
    def estado(self): 
        if self.camina:
            print(f"{self.nombre} está caminando, tiene {self.edad} años, mide {self.altura} cm, su contrato es {self.tipoContrato}, su sueldo es de {self.salario} euros y se encarga de {self.puestoTrabajo}")
        else:
            print(f"{self.nombre} está parado, tiene {self.edad} años, mide {self.altura} cm, su contrato es {self.tipoContrato}, su sueldo es de {self.salario} euros y se encarga de {self.puestoTrabajo}")
           
persona = Persona("Juan", 15, 174, 68)

print(persona.despertar())

persona.estado()

print("\n")
persona.dormir()

persona.caminar()

persona.incrementarEdad(35)

persona.crecerAltura(20) # Prueba persona.crecerAltura(-20)

persona.estado()


empleado = Empleado(1500, "Indefinido", "Pedro", 34, 181, 87)

empleado.caminar()

print("\n")
empleado.estado()

print("\n")
empleado.dormir()

empleado.incrementarEdad(20)

empleado.crecerAltura(10)

empleado.incrementarSalario(300) # Prueba con empleado.incrementarSalario(-600)

empleado.estado()


peon = Peon("Cemento", 1200, "Indefinido", "Jose", 34, 178, 76)

print("\n")
peon.estado()

print("\n")
peon.caminar()

peon.incrementarEdad(15)

peon.crecerAltura(10)

peon.incrementarSalario(-400)

peon.estado()


#print("\n")
#persona.nombre = "Pablo"

#print(persona.nombre) # Olvidate desto, cando hai herencia jódese todo