import sqlite3

miConexion = sqlite3.connect("PrimeraBase") # Crear la conexión

miCursor = miConexion.cursor() # Crear el cursor

#miCursor.execute("CREATE TABLE productos (nombreArticulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

miCursor.execute("INSERT INTO productos VALUES ('Balon', 15, 'Deportes')")

miConexion.commit() # Confirmamos los cambios anteriores (de insertar un registro)

miConexion.close() # Cerra la conexión