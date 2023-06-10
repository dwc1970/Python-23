import tkinter as tk
from PIL import ImageTk, Image

def ingresar():
    # Lógica para el botón de ingresar
    pass

def registrarse():
    # Lógica para el botón de registrarse
    pass

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Usuario")
ventana.geometry("400x300")

# Cargar la imagen de fondo
imagen_fondo = Image.open("sem.jpg")
imagen_fondo = imagen_fondo.resize((400, 300), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear el widget de la imagen de fondo
fondo_label = tk.Label(ventana, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear los botones y las entradas de texto
usuario_label = tk.Label(ventana, text="Usuario:")
usuario_label.place(x=50, y=50)
usuario_entry = tk.Entry(ventana)
usuario_entry.place(x=150, y=50)

contrasena_label = tk.Label(ventana, text="Contraseña:")
contrasena_label.place(x=50, y=100)
contrasena_entry = tk.Entry(ventana, show="*")
contrasena_entry.place(x=150, y=100)

ingresar_button = tk.Button(ventana, text="Ingresar", command=ingresar)
ingresar_button.place(x=150, y=150)

registrarse_button = tk.Button(ventana, text="Registrarse", command=registrarse)
registrarse_button.place(x=250, y=150)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
