import sqlite3
import tkinter as tk
from tkinter import Label




    


conexion=sqlite3.connect("NOMBRES")
curso=conexion.cursor()
# Nos conectamos a la base de datos (si no existe la crea)
conexion = sqlite3.connect("base_prueba.db")
# Creamos (si no existe) una tabla creada alumnos con sus campos
conexion.execute("""create table if not exists alumnos(
                    id integer primary key AUTOINCREMENT,
                    nombre varchar,
                    edad integer
                    )""")
conexion.close()
conexion = sqlite3.connect("base_prueba.db")
# Insertamos dos alumnos

lista=["Ligia","Juan","ELIEZER","SOSA","TORRES","KELLY"]



conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Ligia", 27))
conexion.execute("Insert into alumnos(nombre,edad) values(?,?)", ("Juan", 32))
conexion.execute(" Insert into alumnos(nombre,edad) values(?,?)",('ELIEZER',17))
conexion.execute(" Insert into alumnos(nombre,edad) values(?,?)",('SOSA',15))
conexion.execute(" Insert into alumnos(nombre,edad) values(?,?)",('TORRES',18))
conexion.execute(" Insert into alumnos(nombre,edad) values(?,?)",('KELLY',19))
# Este es necesario para que se ejecuten lñas consultas anteriores
conexion.commit()

# Recuperamos un elementos de la tabla alumnos y lo imprimimos
alumno = conexion.execute("select * from alumnos where nombre = 'Juan'")
alumno=conexion.execute("select * from alumnos where nombre = 'LIGIA'")
alumno=conexion.execute("select * from alumnos where nombre = 'ELIEZER'")
alumno=conexion.execute("select * from alumnos where nombre = 'SOSA'")
alumno=conexion.execute("select * from alumnos where nombre = 'TORRES'")
alumno=conexion.execute("select * from alumnos where nombre = 'KELLY'")
# Esto es para solamente traer el primero o bien para traer uno
fila = alumno.fetchone()
#imprimimos la fila (el alumno)

# Cerramos la conexión con SQLITE

root = tk.Tk()
ro=Label(text=fila)
ro.place(x=40,y=60)
root.geometry("420x380")
root.mainloop()

