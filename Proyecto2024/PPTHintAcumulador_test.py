import random
import time
import sys
import os

def imprimir_texto_dinamico(texto: str, delay: float = 0.1) -> None:
    """
    Imprime texto con un pequeño retardo entre cada letra.

    >>> imprimir_texto_dinamico("Hola", 0)
    Hola
    """
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def borrar_pantalla() -> None:
    """
    Limpia la pantalla, dependiendo del sistema operativo.

    >>> borrar_pantalla() # No podemos probar directamente la limpieza de la pantalla
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def comparar_jugadas(jugador: str, ordenador: str, puntuaciones: list[int]) -> None:
    """
    Compara las jugadas del jugador y el ordenador, actualizando las puntuaciones.

    >>> puntuaciones = [0, 0]
    >>> comparar_jugadas("piedra", "tijeras", puntuaciones)
    Ganaste esta ronda.
    Puntuación: Usuario 1 - Ordenador 0
    >>> comparar_jugadas("papel", "tijeras", puntuaciones)
    Perdiste esta ronda.
    Puntuación: Usuario 1 - Ordenador 1
    >>> comparar_jugadas("papel", "papel", puntuaciones)
    Empate
    Puntuación: Usuario 1 - Ordenador 1
    """
    if jugador == ordenador:
        print("Empate")
    elif (jugador, ordenador) in [("piedra", "tijeras"), ("tijeras", "papel"), ("papel", "piedra")]:
        puntuaciones[0] += 1
        print("Ganaste esta ronda.")
    else:
        puntuaciones[1] += 1
        print("Perdiste esta ronda.")
    print(f"Puntuación: Usuario {puntuaciones[0]} - Ordenador {puntuaciones[1]}")

def jugar() -> tuple[int, int]:
    """
    Ejecuta una partida de "Piedra, Papel o Tijeras", retornando las victorias del usuario y del ordenador.

    >>> random.seed(0)  # Para resultados predecibles en el test
    >>> jugar()
    Elige: 1. Piedra 2. Papel 3. Tijeras
    Tú: tijeras | Ordenador: tijeras
    Empate
    Puntuación: Usuario 0 - Ordenador 0
    Elige: 1. Piedra 2. Papel 3. Tijeras
    Tú: piedra | Ordenador: tijeras
    Ganaste esta ronda.
    Puntuación: Usuario 1 - Ordenador 0
    Elige: 1. Piedra 2. Papel 3. Tijeras
    Tú: papel | Ordenador: tijeras
    Perdiste esta ronda.
    Puntuación: Usuario 1 - Ordenador 1
    El ordenador ganó la partida.
    (0, 1)
    """
    jugadas = ["piedra", "papel", "tijeras"]
    puntuaciones = [0, 0]
    usuario_gana = 0
    ordenador_gana = 0

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
        ordenador = random.choice(jugadas)
        print(f"Tú: {jugador} | Ordenador: {ordenador}")
        comparar_jugadas(jugador, ordenador, puntuaciones)

    if puntuaciones[0] == 3:
        usuario_gana += 1
        print("¡Felicidades! Ganaste la partida.")
    else:
        ordenador_gana += 1
        print("El ordenador ganó la partida.")
   
    return usuario_gana, ordenador_gana

def programa_principal() -> None:
    """
    Ejecuta el menú principal del juego.
   
    >>> random.seed(0)
    >>> programa_principal() # Prueba manual
    """
    total_usuario = 0
    total_ordenador = 0
    while True:
        imprimir_texto_dinamico('"1. Jugar 2. Instrucciones 3. Salir"', 0.02)
        opcion = input("Opción: ")
        if opcion == "1":
            usuario_gana, ordenador_gana = jugar()
            total_usuario += usuario_gana
            total_ordenador += ordenador_gana
            print(f"Resultados totales - Usuario: {total_usuario}, Ordenador: {total_ordenador}")
        elif opcion == "2":
            borrar_pantalla()
            print("Piedra gana a Tijeras, Tijeras a Papel, Papel a Piedra. El primero en 3 gana.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
programa_principal() 