# CRUD = Create Read Update Delete

import sqlite3

miConexion = sqlite3.connect("GestionProductosUnique")

miCursor = miConexion.cursor()


# Read
#miCursor.execute("SELECT * FROM productos WHERE seccion = 'Confeccion'")
#productos = miCursor.fetchall()
#print(productos)


# Update
#miCursor.execute("UPDATE productos SET precio = 35 WHERE nombre_articulo = 'Pelota'")


# Delete
#miCursor.execute("DELETE FROM productos WHERE ID = 5")


miConexion.commit()

miConexion.close()