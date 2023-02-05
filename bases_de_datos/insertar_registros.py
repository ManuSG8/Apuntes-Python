import sqlite3

miConexion = sqlite3.connect("PrimeraBase") 

miCursor = miConexion.cursor() 

#miCursor.execute("CREATE TABLE productos (nombreArticulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

#miCursor.execute("INSERT INTO productos VALUES ('Balon', 15, 'Deportes')")

variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]

miCursor.executemany("INSERT INTO productos VALUES (?,?,?)", variosProductos) # Tantos interrogantes como campos

miConexion.commit() 

miConexion.close() 