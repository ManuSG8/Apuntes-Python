# CONDICIONALES


""" print("Programa de evalución de notas de alumnos")

nota_alumno = input("Introduce la nota del alumno: ") # El input puede estar vacío: input() o llevar un mensaje como en este caso

def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspenso"
    return valoracion

print(evaluacion(4))
print(evaluacion(8))
print(evaluacion(5))
print(evaluacion(int(nota_alumno))) 

# DATO IMPORTANTE: cualquier dato introducido a través del método input() es considerado por defecto como texto (str). Necesitamos transformar los valores (int(),etc.)

# Variables dentro de un bloque
def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspenso"
        calificacion = 7 # Esta variable sólo es accesible desde dentro del condicional IF
    return valoracion """
    


""" print("Verificación de acceso")

edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario < 18:
    print("No puedes pasar")
else:
    print("Puedes pasar")
    
print("El programa ha finalizado") """



""" print("Verificación de acceso")

edad_usuario = int(input("Introduce tu edad: "))

if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")
    
print("El programa ha finalizado") """



""" print("Programa de evalución de notas de alumnos")

nota_alumno = int(input("Introduce tu nota: "))

if nota_alumno < 5:
    print("Insuficiente")
    
elif nota_alumno < 6:
    print("Suficiente")
    
elif nota_alumno < 7:
    print("Bien")
    
elif nota_alumno < 9:
    print("Notable")
    
else: 
    print("Sobresaliente")

print("El programa ha finalizado") """



""" edad = -7

if 0 < edad < 100:
    print("Edad Correcta")
else:
    print("Edad Incorrecta") """
    


""" # Comprobar que los sueldos son mayores de acuerdo al puesto de trabajo

salario_presidente = int(input("Introduce el salario del presidente: "))
print("Salario presidente", salario_presidente) # Alternativa, convertir el entero a cadena de texto: print("Salario presidente " + str(salario_presidente))

salario_director = int(input("Introduce el salario del director: "))
print("Salario director", salario_director)

salario_jefe_area = int(input("Introduce el salario del jefe de area: "))
print("Salario jefe de area", salario_jefe_area)

salario_administrativo = int(input("Introduce el salario del administrativo: "))
print("Salario administrativo", salario_administrativo)

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    
    print("Todo funciona correctamente")
    
else:
    
    print("Algo falla en esta empresa") """
    
    

""" # Comprobar si tiene derecho a beca (la distancia debe ser mayor de 40 km, el número de hermanos debe ser mayor de 2 y el salario de la familia debe ser menor de 20000€)

print("Programa de becas")

distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario anual bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
    
    print("Tienes derecho a beca")
    
else:
    
    print("No tienes derecho a beca") """
    


""" # Comprobar si tiene derecho a beca V2 (la distancia debe ser mayor de 40 km y el número de hermanos debe ser mayor de 2, o el salario de la familia debe ser menor de 20000€)

print("Programa de becas")

distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce el salario anual bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    
    print("Tienes derecho a beca")
    
else:
    
    print("No tienes derecho a beca") """
    
    
""" # Comparador IN

print("Asignaturas optativas")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")

asignatura = input("Escribe la asignatura escogida: ")

if asignatura in ("Informática gráfica", "Pruebas de software", "Usabilidad y accesibilidad"):
    
    print("Asignatura elegida: " + asignatura)
    
else:
    
    print("La asignatura " + asignatura + " no está contemplada") """



""" # DATO IMPORTANTE: Python es case sensitive, es decir: "Pruebas de software" no es igual a "pruebas de software". Cómo solucionarlo:

print("Asignaturas optativas")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower() # Transforma las opciones a minúsculas. pRueBAS dE soFTWaRe = pruebas de software

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"): # Poner los valores a evaluar en minúsculas
    
    print("Asignatura elegida: " + asignatura)
    
else:
    
    print("La asignatura " + asignatura + " no está contemplada") """
    
# FIN CONDICIONALES