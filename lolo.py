import tkinter as tk
import mysql.connector
from tkinter import ttk

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="clientes"
)

mi_cursor = bd.cursor()
mi_cursor.execute("SELECT * from carros")
resultado = mi_cursor.fetchall()

# crear ventana de Tkinter
ventana = tk.Tk()
ventana.title("Lista de carros")

# crear Table
tabla = ttk.Treeview(ventana)
tabla['columns'] = ('matricula', 'modelo','precio','color')

# ajustar las columnas
tabla.column('#0', width=0, stretch=tk.NO)
tabla.column('matricula', anchor=tk.CENTER, width=200)
tabla.column('modelo', anchor=tk.CENTER, width=200)
tabla.column('precio', anchor=tk.CENTER, width=100)
tabla.column('color', anchor=tk.CENTER, width=100)
# heading
tabla.heading('#0', text='', anchor=tk.W)
tabla.heading('matricula', text='matricula', anchor=tk.CENTER)
tabla.heading('modelo', text='modelo', anchor=tk.CENTER)
tabla.heading('precio', text='precio', anchor=tk.CENTER)
tabla.heading('color', text='color', anchor=tk.CENTER)
# agregar datos
for carro in resultado:
  tabla.insert(parent='', index='end', iid=carro[0], values=([0],carro[1],carro[2],carro[3],carro[4],))

# mostrar tabla en ventana
tabla.pack()

ventana.mainloop()
