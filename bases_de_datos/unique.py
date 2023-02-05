import sqlite3

miConexion = sqlite3.connect("GestionProductosUnique")

miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE productos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(50) UNIQUE,
        precio INTEGER,
        seccion VARCHAR(20)
    )
''')

productos = [
    ("Pelota", 20, "Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica"),
    #("Pantalon", 35, "Confeccion") No deja ejecutarlo porque se repite "Pantalon"
]

miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()