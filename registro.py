import tkinter as tk
from tkinter import messagebox

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "admin" and contrasena == "admin":
        resultado.config(text="Inicio de sesión exitoso")
    else:
        messagebox.showwarning(text="Nombre de usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.configure(padx=20)


def ventanita(self):
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('')
    win.configure(background='')
    s3=tk.Label(win,text="BIENVENIDO A LA SEGUNDA VENTANA",bg=" green ",fg="white")
    s3.pack(padx=5,pady=5,ipadx=5,fill=tk.X)
    
    boton2=tk.Button(win,text="ok",command=win.destroy)
    boton2.pack(side=tk.TOP)
    
    
def cerrarventana(self):
    ventanita=tk.Tk()
    ventanita.title("ventana")
    ventanita.geometry('380x300')
    ventanita.configure(background='dark turquoise')
    
    s4=tk.Label(ventanita,text="password",bg="pink",fg="white")
    s4.pack(padx=5,pady=5,ipadx=5,ipady=5)
    nombre_usuario=tk.Entry(ventanita)
    nombre_usuario.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
    
    boton=tk.Button(ventanita,text="neuva",fg="blue",command=ventanita)
    boton.pack(side=tk.TOP)
    
    
    

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack(pady=10)
contrasena_usuario = tk.Entry(ventana, show="*")
contrasena_usuario.pack()

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=10, pady=10)
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
s4=tk.Button(ventana,text="password",command=ventanita)
s4.pack(padx=5,pady=5,ipadx=5,ipady=5)
salir.pack()

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

ventana.config(bg="pink")


ventana.mainloop()