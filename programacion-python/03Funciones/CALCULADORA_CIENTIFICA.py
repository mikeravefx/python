# Calculadora Cientifica en Python
import tkinter as tk
import math

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("600x400")
# Variable para almacenar la expresión matemática
expresion = ""

# Función para actualizar la expresión en la pantalla
def presionar(num):
    global expresion
    expresion += str(num)
    ecuacion.set(expresion)

# Función para evaluar la expresión y mostrar el resultado
def igual():
    try:
        global expresion
        total = str(eval(expresion))
        ecuacion.set(total)
        expresion = total
    except:
        ecuacion.set(" error ")
        expresion = ""

# Función para limpiar la pantalla
def limpiar():
    global expresion
    expresion = ""
    ecuacion.set("")

# Variable StringVar para actualizar la pantalla
ecuacion = tk.StringVar()

# Campo de entrada para mostrar la expresión
pantalla = tk.Entry(ventana, textvariable=ecuacion, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
pantalla.grid(columnspan=4)
# Crear botones numéricos y de operaciones
botones = [
    '7', '8', '9', '/', 'sin', 'cos', 'tan',
    '4', '5', '6', '*', 'log', 'ln', 'sqrt',
    '1', '2', '3', '-', '(', ')', '^',
    '0', '.', '=', '+', 'C'
]

fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        tk.Button(ventana, text=boton, padx=20, pady=20, font=('Arial', 18), command=igual).grid(row=fila, column=columna, columnspan=2)
        columna += 2
    elif boton == "C":
        tk.Button(ventana, text=boton, padx=20, pady=20, font=('Arial', 18), command=limpiar).grid(row=fila, column=columna, columnspan=2)
        columna += 2
    else:
        tk.Button(ventana, text=boton, padx=20, pady=20, font=('Arial', 18), command=lambda boton=boton: presionar(boton)).grid(row=fila, column=columna)
        columna += 1
        if columna > 6:
            columna = 0
            fila += 1
            # Ejecutar la ventana principal
ventana.mainloop()