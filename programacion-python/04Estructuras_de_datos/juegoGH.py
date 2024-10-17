import tkinter as tk
import random

# Función para determinar el ganador
def determinar_ganador(eleccion_jugador):
    opciones = ["Piedra", "Papel", "Tijera"]
    eleccion_computadora = random.choice(opciones)
    resultado = ""

    if eleccion_jugador == eleccion_computadora:
        resultado = "Empate"
    elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel"):
        resultado = "¡Ganaste!"
    else:
        resultado = "Perdiste"

    etiqueta_resultado.config(text=f"Computadora eligió: {eleccion_computadora}\n{resultado}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

# Etiqueta de instrucciones
etiqueta_instrucciones = tk.Label(ventana, text="Elige una opción:")
etiqueta_instrucciones.pack()

# Botones para las opciones
boton_piedra = tk.Button(ventana, text="Piedra", command=lambda: determinar_ganador("Piedra"))
boton_piedra.pack()

boton_papel = tk.Button(ventana, text="Papel", command=lambda: determinar_ganador("Papel"))
boton_papel.pack()

boton_tijera = tk.Button(ventana, text="Tijera", command=lambda: determinar_ganador("Tijera"))
boton_tijera.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()