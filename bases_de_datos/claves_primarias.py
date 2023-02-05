import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE productos (
        codigo_articulo VARCHAR(4) PRIMARY KEY,
        nombre_articulo VARCHAR(50),
        precio INTEGER,
        seccion VARCHAR(20)
    )
''') # Con las comillas nos permite escribir en varias lineas

productos = [
    ("AR01", "Pelota", 20, "Jugueteria"),
    ("AR02", "Pantalon", 15, "Confeccion"),
    ("AR03", "Destornillador", 25, "Ferreteria"),
    ("AR04", "Jarron", 45, "Ceramica")
]

miCursor.executemany("INSERT INTO productos VALUES (?,?,?,?)", productos)

miConexion.commit()

miConexion.close()

# Si queremos crear un ID automático
"""miCursor.execute('''
    CREATE TABLE productos (
        idArticulo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(50),
        precio INTEGER,
        seccion VARCHAR(20)
    )
''')

productos = [
    ("Pelota", 20, "Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica")
]

miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", productos)"""