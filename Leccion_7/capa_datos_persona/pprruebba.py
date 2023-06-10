import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self):
        self.preguntas = [["CATEGORIA: Python: ¿Cómo le llamamos en Python a la tabulación dentro de una estructura de control if/else o también dentro de un bucle?",
                           "[1] Identacion",
                           "[2] Format",
                           "[3] Interpolacion",
                           "[4] Ninguna de las anteriores",
                           "1"],
                          ["CATEGORIA: Python: ¿Qué utilizamos para saber que es una Tupla?",
                           "[1] Llaves",
                           "[2] Corchetes",
                           "[3] Parentesis",
                           "[4] Comillas",
                           "3"],
                          # Resto de las preguntas aquí...
                         ]
        self.respuesta = ""
        self.rpta = ""
        self.puntaje = 0
        self.num_pregunta = 0

    def mostrar_pregunta(self):
        pregunta_actual = self.preguntas[self.num_pregunta]
        respuesta = messagebox.askquestion("Pregunta", pregunta_actual[0] + "\n" + pregunta_actual[1] + "\n" + pregunta_actual[2] + "\n" + pregunta_actual[3] + "\n" + pregunta_actual[4])
        self.respuesta = respuesta
        self.rpta = pregunta_actual[5]
        self.validar_respuesta()

    def validar_respuesta(self):
        if self.respuesta == self.rpta:
            self.puntaje += 10
            print("Correcto!")
        else:
            print("Incorrecto!")
        self.num_pregunta += 1
        if self.num_pregunta < len(self.preguntas):
            self.mostrar_pregunta()
        else:
            self.calcular_ganador()

    def calcular_ganador(self):
        if self.puntaje >= 70:
            print("You win")
            print("Tu puntaje es:", self.puntaje)
        else:
            print("You lose")
            print("Tu puntaje es:", self.puntaje)

# Crear una instancia de la clase Question
question = Question()

# Crear la ventana principal de tkinter
window = tk.Tk()
window.title("Juego de preguntas")
window.geometry("400x200")

# Función para mostrar la pregunta al hacer clic en el botón
def mostrar_pregunta():
    question.mostrar_pregunta()

# Crear un botón en la ventana
button = tk.Button(window, text="Mostrar pregunta", command=mostrar_pregunta)
button.pack()

# Iniciar el bucle principal de tkinter
window.mainloop()
