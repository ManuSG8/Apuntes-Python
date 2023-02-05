from setuptools import setup

setup(
    
    name = "paqueteCalculos", # El nombre que quieras
    version = "1.0", # La que tú quieras
    description = "Paquete de redondeo y potencia", # La que tú quieras
    author = "Manu", # El nombre que tú quieras
    author_email = "manu-sg8@hotmail.com", # Opcional
    url = "www.manu.com", # Opcional
    packages = ["paquete","paquete.redondeo_potencia"] # Indicar donde se encuentra el paquete o subpaquete que queremos. Sintaxis: packages=["nombre_paquete","nombre_paquete.nombre_subpaquete",...]

) # Cuidado con las comas