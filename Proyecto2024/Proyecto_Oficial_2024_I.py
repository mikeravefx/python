import random
import time
import sys
import os

def imprimir_texto_dinamico(texto, delay=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Nueva línea al final del texto

def borrar_pantalla():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y macOS
        os.system('clear')

def obtener_jugada_ordenador(jugada_jugador: int, modo_trampa: bool) -> int:
    """Devuelve la jugada que el ordenador debe elegir. En modo trampa, siempre elige la que gana."""
    if modo_trampa:
        # Modo trampa: el ordenador siempre elige la jugada ganadora.
        if jugada_jugador == 1:  # Piedra
            return 2  # Papel
        elif jugada_jugador == 2:  # Papel
            return 3  # Tijeras
        elif jugada_jugador == 3:  # Tijeras
            return 1  # Piedra
    else:
        # Modo normal: el ordenador juega aleatoriamente.
        return random.choice([1, 2, 3])

def comparar_jugadas(jugada_jugador: int, jugada_ordenador: int) -> tuple:
    """Compara las jugadas del jugador y el ordenador, y retorna las puntuaciones actualizadas."""
    puntuacion_usuario = 0
    puntuacion_ordenador = 0

    if jugada_jugador == jugada_ordenador:
        print("Empate")
    elif (jugada_jugador == 1 and jugada_ordenador == 3) or \
         (jugada_jugador == 3 and jugada_ordenador == 2) or \
         (jugada_jugador == 2 and jugada_ordenador == 1):
        puntuacion_usuario += 1
        print("Ganaste esta ronda.")        
    else:
        puntuacion_ordenador += 1
        print("Perdiste esta ronda.")

    return puntuacion_usuario, puntuacion_ordenador

def jugar(modo_trampa: bool) -> None:
    puntuacion_usuario = 0
    puntuacion_ordenador = 0
    activartrampa = False

    while puntuacion_usuario < 3 and puntuacion_ordenador < 3:
        imprimir_texto_dinamico('''\nElige una opción:\n1. Piedra\n2. Papel\n3. Tijeras\n''', delay=0.02)

        try:
            eleccion = int(input("Tu elección (1-3): "))
            if eleccion < 1 or eleccion > 3:
                raise ValueError("Opción no válida")
        except ValueError as e:
            print(e)
            continue
       
        jugada_jugador = eleccion
       
        # El ordenador elige su jugada, en modo trampa elige la que siempre gana
        jugada_ordenador = obtener_jugada_ordenador(jugada_jugador, activartrampa)

        if modo_trampa and puntuacion_usuario == 2:
            activartrampa = True
            imprimir_texto_dinamico("¡Oh no! El ordenador está trampeando... ¡Escojo mi jugada!")
        else:
            imprimir_texto_dinamico(f"El ordenador elige: {jugada_ordenador}")

        # Convertimos la jugada a texto para la visualización
        opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
        print("Tú elegiste:", opciones[jugada_jugador])
        print("Ordenador eligió:", opciones[jugada_ordenador])

        # Actualizamos las puntuaciones
        puntuacion_usuario_ronda, puntuacion_ordenador_ronda = comparar_jugadas(jugada_jugador, jugada_ordenador)
        puntuacion_usuario += puntuacion_usuario_ronda
        puntuacion_ordenador += puntuacion_ordenador_ronda

        print("Puntuación total: Usuario", puntuacion_usuario, "- Ordenador", puntuacion_ordenador)

    if puntuacion_usuario == 3:
        print("¡Felicidades! Ganaste la partida.")
        print("Puntuación total: Usuario", puntuacion_usuario, "- Ordenador", puntuacion_ordenador)
    else:
        print("El ordenador ganó la partida. ¡Mejor suerte la próxima vez!")
        print("Puntuación total: Usuario", puntuacion_usuario, "- Ordenador", puntuacion_ordenador)

def programaprincipal() -> None:
    while True:
        imprimir_texto_dinamico('''\nMenú:\n1. Jugar\n2. Ver instrucciones\n3. Elegir modo\n4. Salir\n''', delay=0.02)
       
        try:
            opcion = int(input("Elige una opción (1-4): "))
        except ValueError:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        if opcion == 1:
            jugar(False)
        elif opcion == 2:
            print('''\nInstrucciones:
1. Piedra vence a tijeras
2. Papel vence a piedra
3. Tijeras vence a papel
Elige tu opción y compite contra el ordenador. El primer jugador en ganar 3 rondas es el vencedor.\n''')
        elif opcion == 3:
            imprimir_texto_dinamico("Elige el modo de juego:\n1. Normal\n2. Trampa", delay=0.02)
            try:
                modo = int(input("Elige una opción (1-2): "))
                if modo == 1:
                    jugar(False)
                elif modo == 2:
                    jugar(True)
                else:
                    print("Opción no válida. Regresando al menú principal.")
            except ValueError:
                print("Opción no válida. Regresando al menú principal.")
        elif opcion == 4:
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar programa principal
programaprincipal()