import sqlite3

conexion=sqlite3.connect(" PRUEBA02 ")

curso=conexion.cursor()

curso.execute("""
    CREATE TABLE VEHICULOS (
        MATRICULA VARCHAR  PRIMARY KEY,
        MODELO VARCHAR
        PRECIO INTEGER
        COLOR VARCHAR
        )
""")

añadir_datos = [
    ("5514-DSK","MERCEDES","5000","GRIS"),
    ("1234-SCD","SEAT","1000","ROJO"),
    ("9812-FGV","RENAULT","2000","AMARILLO"),
    ("9898-KLS","SEAT","2000","AZUL")
    ("1243-CCX","BPW","35000","MARRON")
]

curso.executemany("INSERT INTO VEHICULOS VALUES (?,?,?,?)",añadir_datos)

conexion.commit()

conexion.close()
