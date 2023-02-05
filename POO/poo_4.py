# POO IV

# HERENCIA


""" class Vehiculos():
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
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}")
        
        
class Moto(Vehiculos):
    pass


miMoto = Moto("Honda", "CBR")

miMoto.estado() """  



""" # Sobreescritura de métodos

class Vehiculos():
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
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}")
        
        
class Moto(Vehiculos):
    
    hcaballito = ""
    
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
        
    def estado(self): # Para sobreescribir un método, le ponemos el mismo nombre que en la clase padre, y con el mismo número de parámetros. Este método anula el método en la clase moto de la clase padre
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}\n{self.hcaballito}")


miMoto = Moto("Honda", "CBR")

miMoto.caballito() # Si no se ejecuta esta línea, no mostraría nada. Porque al no llamar al método caballito, nunca se ejecutará el método

miMoto.estado()

# IMPORTANTE: Si creamos otro objeto, por ejemplo el objeto Quad, que herede de la clase Moto, 
# heredará de la clase Moto y de la clase Vehiculos. Pero el método estado() lo heredará de la clase Moto """



""" class Vehiculos():
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
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}")


class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
        
        
        
class Moto(Vehiculos):
    
    hcaballito = ""
    
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
        
    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}\n{self.hcaballito}")


miMoto = Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()


miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True)) """



""" # Herencia múltiple

class Vehiculos():
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
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}")


class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
        
        
        
class Moto(Vehiculos):
    
    hcaballito = ""
    
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
        
    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}\n{self.hcaballito}")


class VElectricos():
    
    def __init__(self):
        self.autonomia = 100
        
    def cargarEnergia(self):
        self.cargando = True


miMoto = Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()


miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectricos,Vehiculos): # Herencia múltiple
    pass


miBici = BicicletaElectrica() # En la herencia múltiple, se da preferencia a la primera clase, en este caso VElectricos. Por lo cuál no debemos pasarle ningún parámetro """



""" # Función super() y isinstance(objeto, clase)

class Persona():
    
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
        
    def descripcion(self):
        print("Nombre: ",self.nombre," Edad: ",self.edad," Residencia: ",self.lugar_residencia)


class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # Está llamando al método __init__() de la clase padre
        
        self.salario = salario
        self.antiguedad = antiguedad
        
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario," Antiguedad: ",self.antiguedad)      


antonio = Empleado(1500, 15, "Antonio", "55", "Colombia")  

antonio.descripcion()

print(isinstance(antonio, Persona)) # Sintaxis: isinstance(nombre_objeto, nombre_clase). Nos dice si un objeto pertenece a una clase. Ojo con el principio de sustitución """



""" class Vehiculos():
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
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}")


class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
        
        
        
class Moto(Vehiculos):
    
    hcaballito = ""
    
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
        
    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nMarca: {self.frena}\n{self.hcaballito}")


class VElectricos(Vehiculos):
      
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
        
    def cargarEnergia(self):
        self.cargando = True
        
    def estado(self):
        super().estado()


miMoto = Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()


miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectricos,Vehiculos):
    pass


miBici = BicicletaElectrica("Orbea", "H1030")

miBici.estado() """

# FIN POO IV