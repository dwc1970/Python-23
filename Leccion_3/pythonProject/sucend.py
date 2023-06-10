import tkinter as tk
from tkinter import messagebox
import pandas as pd
import openpyxl
from openpyxl import Workbook

# Crear una ventana principal
root = tk.Tk()
root.title("S.U.C.E.N.D")
root.geometry("700x300")
root.config(bg="GREEN") # Establecer el fondo de la ventana como azul

# Crear un DataFrame
df = pd.DataFrame(columns=["usuario", "contraseña", "correo electrónico"])

# Funciones
def registrar():
    usuario = usuario_entry.get().lower().replace(" ", "")  # El usuario es su nombre y apellido sin espacios
    contrasena = contrasena_entry.get()  # La contraseña es su número de DNI
    confirmar_contrasena = confirmar_contrasena_entry.get()
    correo = correo_entry.get() # Obtener el correo electrónico ingresado

    # Validar campos vacios
    if not usuario or not contrasena or not confirmar_contrasena or not correo:
        messagebox.showerror("Error", "Todos los campos son requeridos")
        return

    # Validar contraseña
    if contrasena != confirmar_contrasena:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return

    # Validar si el usuario ya existe
    if usuario in df["usuario"].values:
        messagebox.showerror("Error", "El usuario ya existe")
        return

    # Agregar usuario, contraseña y correo electrónico al DataFrame
    df.loc[len(df)] = [usuario, contrasena, correo]

    # Guardar DataFrame en un archivo Excel
    wb = openpyxl.load_workbook("datos_Celador.xlsx")
    ws = wb.active
    for row in df.iterrows():
        row_values = list(row[1])
        ws.append(row_values)
    wb.save("datos_Celador.xlsx")

    # Mostrar mensaje de éxito y borrar campos del registro
    messagebox.showinfo("Registro", "Usuario registrado exitosamente")
    usuario_entry.delete(0, tk.END)
    contrasena_entry.delete(0, tk.END)
    confirmar_contrasena_entry.delete(0, tk.END)
    correo_entry.delete(0, tk.END)

# Crear etiquetas y campos de entrada
usuario_label = tk.Label(root, text="Usuario:")
usuario_label.grid(row=0, column=0, padx=10, pady=10)
usuario_entry = tk.Entry(root, width=30)
usuario_entry.grid(row=0, column=1, padx=10, pady=10)

contrasena_label = tk.Label(root, text="Contraseña:")
contrasena_label.grid(row=1, column=0, padx=10, pady=10)
contrasena_entry = tk.Entry(root, show="*", width=30)
contrasena_entry.grid(row=1, column=1, padx=10, pady=10)

confirmar_contrasena_label = tk.Label(root, text="Confirmar contraseña:")
confirmar_contrasena_label.grid(row=2, column=0, padx=10, pady=10)
confirmar_contrasena_entry = tk.Entry(root, show="*", width=30)
confirmar_contrasena_entry.grid(row=2, column=1, padx=10, pady=10)

correo_label = tk.Label(root, text="Correo electrónico:")
correo_label.grid(row=3, column=0, padx=10, pady=10)
correo_entry = tk.Entry(root, width=30)
correo_entry.grid(row=3, column=1, padx=10, pady=10)
# Crear etiquetas y campos de entrada
usuario_label = tk.Label(root, text="Usuario (nombre y apellido sin espacios en minúscula):")
usuario_label.grid(row=0, column=0, padx=10, pady=10)
usuario_entry = tk.Entry(root, width=30)
usuario_entry.grid(row=0, column=1, padx=10, pady=10)

contrasena_label = tk.Label(root, text="Contraseña (DNI):")
contrasena_label.grid(row=1, column=0, padx=10, pady=10)
contrasena_entry = tk.Entry(root, show="*", width=30)
contrasena_entry.grid(row=1, column=1, padx=10, pady=10)

confirmar_contrasena_label = tk.Label(root, text="Confirmar contraseña:")
confirmar_contrasena_label.grid(row=2, column=0, padx=10, pady=10)
confirmar_contrasena_entry = tk.Entry(root, show="*", width=30)
confirmar_contrasena_entry.grid(row=2, column=1, padx=10, pady=10)

correo_label = tk.Label(root, text="Correo electrónico:")
correo_label.grid(row=3, column=0, padx=10, pady=10)
correo_entry = tk.Entry(root, width=30)
correo_entry.grid(row=3, column=1, padx=10, pady=10)

# Funciones
def registrar():
    usuario = usuario_entry.get().replace(" ", "").lower()
    contrasena = contrasena_entry.get()
    confirmar_contrasena = confirmar_contrasena_entry.get()
    correo = correo_entry.get() # Obtener el correo electrónico ingresado

    # Validar campos vacios
    if not usuario or not contrasena or not confirmar_contrasena or not correo:
        messagebox.showerror("Error", "Todos los campos son requeridos")
        return

    # Validar contraseña
    if contrasena != confirmar_contrasena:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return

    # Validar si el usuario ya existe
    if usuario in df["usuario"].values:
        messagebox.showerror("Error", "El usuario ya existe")
        return

    # Agregar usuario, contraseña y correo electrónico al DataFrame
    df.loc[len(df)] = [usuario, contrasena, correo]

    # Guardar DataFrame en un archivo Excel
    wb = openpyxl.load_workbook("datos_Celador.xlsx")
    ws = wb.active
    for row in df.iterrows():
        row_values = list(row[1])
        ws.append(row_values)
    wb.save("datos_Celador.xlsx")

    # Mostrar mensaje de éxito y borrar campos del registro
    messagebox.showinfo("Registro", "Usuario registrado exitosamente")
    usuario_entry.delete(0, tk.END)
    contrasena_entry.delete(0, tk.END)
    confirmar_contrasena_entry.delete(0, tk.END)
    correo_entry.delete(0, tk.END)

# Crear botón de registro
registrar_btn = tk.Button(root, text="Registrarse", command=registrar)
registrar_btn.place(x=200, y=200)

# Iniciar el loop principal
root.mainloop()
