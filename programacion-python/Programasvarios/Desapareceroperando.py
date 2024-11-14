import random

def generar_operacion():
    tipo_operacion = random.choice(["multiplicacion", "suma", "resta"])
    operando1 = random.randint(0, 10)
    operando2 = random.randint(0, 10)

    if tipo_operacion == "multiplicacion":
        respuesta_correcta = operando1 * operando2
    elif tipo_operacion == "+":
        respuesta_correcta = operando1 + operando2
    else:
        respuesta_correcta = operando1 - operando2

    return operando1, operando2, tipo_operacion, respuesta_correcta

def modo_dificil(operando1, operando2, operacion, respuesta_correcta):
    pregunta_tipo = random.choice(["resultado", "operando1", "operando2"])

    if pregunta_tipo == "resultado":
        print(f"¿Cuánto es {operando1} {operacion} {operando2}?")
        respuesta_usuario = int(input("Respuesta: "))
        return respuesta_usuario == respuesta_correcta
    elif pregunta_tipo == "operando1":
        print(f"¿Qué número falta? ___ {operacion} {operando2} = {respuesta_correcta}")
        respuesta_usuario = int(input("Respuesta: "))
        return respuesta_usuario == operando1
    else:
        print(f"¿Qué número falta? {operando1} {operacion} ___ = {respuesta_correcta}")
        respuesta_usuario = int(input("Respuesta: "))
        return respuesta_usuario == operando2

def juegonumerico():
    vidas = 3
    puntuacion = 0

    while vidas > 0:
        operando1, operando2, operacion, respuesta_correcta = generar_operacion()

        if modo_dificil(operando1, operando2, operacion, respuesta_correcta):
            puntuacion += 1
            print("¡Correcto!")
        else:
            vidas -= 1
            print(f"Incorrecto. La respuesta correcta es {respuesta_correcta}. Te quedan {vidas} vidas.")

        print(f"Puntuación: {puntuacion}")

    print("Juego terminado. ¡Gracias por jugar!")


juegonumerico()
