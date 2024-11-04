import random

def generar_operacion():
    tipo_operacion = random.choice(["multiplicacion", "suma", "resta"])
    operando1 = random.randint(0, 10)
    operando2 = random.randint(0, 10)

    if tipo_operacion == "multiplicacion":
        return operando1, operando2, "*"
    elif tipo_operacion == "suma":
        return operando1, operando2, "+"
    else:
        return operando1, operando2, "-"

def prueba():
    vidas = 3
    puntuacion = 0

    while vidas > 0:
        operando1, operando2, operacion = generar_operacion()
        
        if operacion == "*":
            respuesta_correcta = operando1 * operando2
        elif operacion == "+":
            respuesta_correcta = operando1 + operando2
        else:
            respuesta_correcta = operando1 - operando2

        print(f"¿Cuánto es {operando1} {operacion} {operando2}?")
        respuesta_usuario = int(input("Respuesta: "))

        if respuesta_usuario == respuesta_correcta:
            puntuacion += 1
            print("¡Correcto!")
        else:
            vidas -= 1
            print(f"Incorrecto. La respuesta correcta es {respuesta_correcta}. Te quedan {vidas} vidas.")

        print(f"Puntuación: {puntuacion}")

    print("Juego terminado. ¡Gracias por jugar!")

prueba()
