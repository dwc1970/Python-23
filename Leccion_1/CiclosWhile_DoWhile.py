import tkinter as tk

def ciclo_while():
    contador = 0
    resultado_while.delete(1.0, tk.END)
    numero = int(entrada_numero.get())
    while contador < numero:
        resultado_while.insert(tk.END, "El contador es " + str(contador) + "\n")
        contador += 1
    resultado_while.insert(tk.END, "Fin del ciclo while.")

def ciclo_do_while():
    contador = 0
    resultado_do_while.delete(1.0, tk.END)
    numero = int(entrada_numero.get())
    while True:
        resultado_do_while.insert(tk.END, "El contador es " + str(contador) + "\n")
        contador += 1
        if contador >= numero:
            break
    resultado_do_while.insert(tk.END, "Fin del ciclo do-while.")

ventana = tk.Tk()
ventana.title("Ejemplo de ciclos")
ventana.geometry("500x500")

# Crear cuadro de entrada de datos
label_numero = tk.Label(ventana, text="Ingrese un número:")
label_numero.pack(pady=10)
entrada_numero = tk.Entry(ventana)
entrada_numero.pack(pady=5)

# Crear botones para llamar a las funciones de los ciclos
boton_while = tk.Button(ventana, text="Mostrar ciclo while", command=ciclo_while)
boton_do_while = tk.Button(ventana, text="Mostrar ciclo do-while", command=ciclo_do_while)

# Crear cuadros de texto para mostrar los resultados
resultado_while = tk.Text(ventana)
resultado_do_while = tk.Text(ventana)

# Posicionar los elementos en la ventana
boton_while.pack(pady=10)
resultado_while.pack(fill=tk.BOTH, expand=True)
boton_do_while.pack(pady=10)
resultado_do_while.pack(fill=tk.BOTH, expand=True)

ventana.mainloop()
