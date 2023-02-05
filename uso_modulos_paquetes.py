# CÓMO UTILIZAR LOS MÓDULOS QUE ESTÁN EN LOS PAQUETES

from paquete.calculos_generales import * # Sintaxis: from nombre_paquete.nombre_modulo import (nombre_funcion || *)

potencia(4,6)
sumar(3,4)
redondear(6.55)

# Se pueden crear subcarpetas dentro de un paquete (hay que incluír el archivo __init__.py vacío en cada una de ellas). 
# Para llamar a esos módulos: from nombre_paquete.nombre_subpaquete.nombre_modulo import (nombre_funcion || *)
from paquete.calculos_basicos.basicos import *
sumar(4,7)

from paquete.redondeo_potencia.redondeaYpotencia import potencia
potencia(3,4)
