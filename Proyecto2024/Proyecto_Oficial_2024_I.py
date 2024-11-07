import random
import time
import sys
from typing import Tuple

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

def obtener_jugada_ordenador(jugada_jugador: str, modo_trampa: bool) -> str:
    """Devuelve la jugada que el ordenador debe elegir. En modo trampa, siempre elige la que gana."""
    if modo_trampa and jugada_jugador <= 2:
        # Modo trampa: el ordenador siempre elige la jugada ganadora.
        if jugada_jugador == "piedra":
            return "papel"
        elif jugada_jugador == "papel":
            return "tijeras"
        elif jugada_jugador == "tijeras":
            return "piedra"
    else:
        # Modo normal: el ordenador juega aleatoriamente.
        return random.choices(["piedra", "papel", "tijeras"])
    

def comparar_jugadas(jugada_jugador: str, jugada_ordenador: str) -> tuple:
    """Compara las jugadas del jugador y el ordenador, y retorna las puntuaciones actualizadas."""
    puntuacion_usuario = 0
    puntuacion_ordenador = 0

    if jugada_jugador == jugada_ordenador:
        print("Empate")
    elif (jugada_jugador == "piedra" and jugada_ordenador == "tijeras") or \
         (jugada_jugador == "tijeras" and jugada_ordenador == "papel") or \
         (jugada_jugador == "papel" and jugada_ordenador == "piedra"):
        puntuacion_usuario += 1
        print("Ganaste esta ronda.")         
    else:
        puntuacion_ordenador += 1
        print("Perdiste esta ronda.")

    return puntuacion_usuario, puntuacion_ordenador

def jugar(modo_trampa: bool) -> None:
    posiblesjugadas = ["piedra", "papel", "tijeras"]
    puntuacion_usuario = 0
    puntuacion_ordenador = 0

    while puntuacion_usuario < 3 and puntuacion_ordenador < 3:
        imprimir_texto_dinamico('''\nElige una opción:\n"1. Piedra"\n"2. Papel"\n"3. Tijeras''', delay=0.00001)

        try:
            eleccion = int(input("Tu elección: "))
            if eleccion < 1 or eleccion > 3:
                raise ValueError("Opción no válida")
        except ValueError as e:
            print(e)
            continue
        
        jugada_jugador = posiblesjugadas[eleccion - 1]
        
        # El ordenador elige su jugada, en modo trampa elige lo que siempre gana
        jugada_ordenador = random.choices(obtener_jugada_ordenador(jugada_jugador, modo_trampa = False))

        if modo_trampa and puntuacion_usuario == 2:
            imprimir_texto_dinamico(f"¡Oh no! El ordenador está trampeando... ¡Escojo mi jugada!")
        else:
            imprimir_texto_dinamico(f"El ordenador elige: {jugada_ordenador}")

        print("Tú elegiste:", jugada_jugador)
        print("Ordenador eligió:", jugada_ordenador)

        # Actualizamos las puntuaciones
        puntuacion_usuario_ronda, puntuacion_ordenador_ronda = comparar_jugadas(jugada_jugador, jugada_ordenador)
        puntuacion_usuario += puntuacion_usuario_ronda
        puntuacion_ordenador += puntuacion_ordenador_ronda

        print("Puntuación total: Usuario", puntuacion_usuario, "- Ordenador", puntuacion_ordenador)

    if puntuacion_usuario == 3:
        print("¡Felicidades! Ganaste la partida.")
    else:
        print("El ordenador ganó la partida. ¡Mejor suerte la próxima vez!")

def programaprincipal() -> None:
    while True:
        imprimir_texto_dinamico('''"Menú:"\n"1. Jugar"\n"2. Ver instrucciones"\n"3. Elegir modo"\n"4. Salir"''', delay=0.02)
        opciones_validas = ("1", "2", "3", "4")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Jugar con el modo trampa desactivado
            jugar(False)
        elif opcion == "2":
            print('''"\nInstrucciones:"\n"1. Piedra vence a tijeras"
                          \n"2. Papel vence a piedra"
                          \n"3. Tijeras vence a papel"
                          \n"Elige tu opción y compite contra el ordenador. El primer jugador en ganar 3 rondas es el vencedor.\n"''')
        elif opcion == "3":
            # Elegir modo de juego: normal o trampa
            imprimir_texto_dinamico("Elige el modo de juego:\n1. Normal\n2. Trampa", delay=0.02)
            modo = input("Elige una opción: ")
            if modo == "1":
                jugar(False)
            elif modo == "2":
                jugar(True)
            else:
                print("Opción no válida. Regresando al menú principal.")
        elif opcion == "4":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar programa principal
programaprincipal()

