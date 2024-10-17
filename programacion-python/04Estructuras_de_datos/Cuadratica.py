import tkinter as tk
from tkinter import messagebox
import math

# Función para calcular las soluciones de la ecuación de segundo grado
def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        discriminante = b**2 - 4*a*c
        
        if discriminante < 0:
            resultado = "No hay soluciones reales"
        elif discriminante == 0:
            x = -b / (2*a)
            resultado = f"Una solución: x = {x}"
        else:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            resultado = f"Dos soluciones: x1 = {x1}, x2 = {x2}"
        
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuaciones de Segundo Grado")

# Etiquetas y campos de entrada para los coeficientes
tk.Label(ventana, text="Coeficiente a:").grid(row=0, column=0)
entry_a = tk.Entry(ventana)
entry_a.grid(row=0, column=1)

tk.Label(ventana, text="Coeficiente b:").grid(row=1, column=0)
entry_b = tk.Entry(ventana)
entry_b.grid(row=1, column=1)

tk.Label(ventana, text="Coeficiente c:").grid(row=2, column=0)
entry_c = tk.Entry(ventana)
entry_c.grid(row=2, column=1)

# Botón para calcular las soluciones
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=3, columnspan=2)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()