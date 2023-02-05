import sqlite3

miConexion = sqlite3.connect("PrimeraBase") 

miCursor = miConexion.cursor() 

miCursor.execute("SELECT * FROM productos")

variosProductos = miCursor.fetchall()

for producto in variosProductos:
    print("Nombre Articulo: ",producto[0]," Seccion: ",producto[2])

miConexion.commit() 

miConexion.close() 