# LLAMAR MÓDULOS

""" import crear_modulos # Se importa el módulo (nombre del archivo)

crear_modulos.sumar(3,4) # Sintaxis: nombres_archivo.nombre_funcion(parámetros) """



""" from crear_modulos import sumar # De este modo no tenemos que usar el método del punto

sumar(7,5) """



from crear_modulos import * # Con el asterisco, importamos todas las funciones

sumar(4,3)
restar(3,1)
multiplicar(2,5)