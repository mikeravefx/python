
import random

import time

import sys

import os



def imprimir_texto_dinamico(texto: str, delay: float = 0.1) -> None:

    for letra in texto:

        sys.stdout.write(letra)

        sys.stdout.flush()

        time.sleep(delay)

    print()



def borrar_pantalla() -> None:

    os.system('cls' if os.name == 'nt' else 'clear')



def comparar_jugadas(jugador: str, ordenador: str, puntuaciones: list[int]) -> None:

    if jugador == ordenador:

        print("Empate")

    elif (jugador, ordenador) in [("piedra", "tijeras"), ("tijeras", "papel"), ("papel", "piedra")]:

        puntuaciones[0] += 1

        print("Ganaste esta ronda.")

    else:

        puntuaciones[1] += 1

        print("Perdiste esta ronda.")

    print(f"Puntuación: Usuario {puntuaciones[0]} - Ordenador {puntuaciones[1]}")



def jugar() -> None:

    jugadas = ["piedra", "papel", "tijeras"]

    puntuaciones = [0, 0]

    while max(puntuaciones) < 3:

        imprimir_texto_dinamico('\nElige: 1. Piedra 2. Papel 3. Tijeras', 0.02)

        try:

            eleccion = int(input("Tu elección (1-3): "))

            if eleccion not in [1, 2, 3]:

                raise ValueError

        except ValueError:

            print("Elección inválida. Inténtalo de nuevo.")

            continue



        jugador = jugadas[eleccion - 1]

        ordenador = random.randint(jugadas)
        # Jugada repepetitiva predesible
        # Jugada predesible
        # ordenador = random.choice(jugadas)

        print(f"Tú: {jugador} | Ordenador: {ordenador}")

        comparar_jugadas(jugador, ordenador, puntuaciones)

    

    ganador = "Usuario" if puntuaciones[0] == 3 else "Ordenador"

    print(f"¡{ganador} ganó la partida!")



def programa_principal() -> None:

    while True:

        imprimir_texto_dinamico('"1. Jugar 2. Instrucciones 3. Salir"', 0.02)

        opcion = input("Opción: ")

        if opcion == "1":

            jugar()

        elif opcion == "2":

            borrar_pantalla()

            print("Piedra gana a Tijeras, Tijeras a Papel, Papel a Piedra. El primero en 3 gana.")

        elif opcion == "3":

            print("¡Hasta luego!")

            break

        else:

            print("Opción inválida. Intenta de nuevo.")

programa_principal()







 
