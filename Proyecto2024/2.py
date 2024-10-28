import random

def generar_operacion():
    operando1 = random.randint(0, 10)
    operando2 = random.randint(0, 10)
    return operando1, operando2

def juego():
    vidas = 3
    puntuacion = 0

    while vidas > 0:
        operando1, operando2 = generar_operacion()
        respuesta_correcta = operando1 * operando2

        print(f"¿Cuánto es {operando1} x {operando2}?")
        respuesta_usuario = int(input("Respuesta: "))

        if respuesta_usuario == respuesta_correcta:
            puntuacion += 1
            print("¡Correcto!")
        else:
            vidas -= 1
            print(f"Incorrecto. La respuesta correcta es {respuesta_correcta}. Te quedan {vidas} vidas.")

        print(f"Puntuación: {puntuacion}")

    print("Juego terminado. ¡Gracias por jugar!")

juego()
