# test_juego.py

import doctest



def comparar_jugadas(jugador: str, ordenador: str, puntuaciones: list[int]) -> None:
    """
    Compara las jugadas del jugador y el ordenador.

    >>> puntuaciones = [0, 0]
    >>> comparar_jugadas('piedra', 'tijeras', puntuaciones)
    Ganaste esta ronda.
    >>> puntuaciones
    [1, 0]

    >>> puntuaciones = [0, 0]
    >>> comparar_jugadas('papel', 'tijeras', puntuaciones)
    Perdiste esta ronda.
    >>> puntuaciones
    [0, 1]

    >>> puntuaciones = [0, 0]
    >>> comparar_jugadas('piedra', 'piedra', puntuaciones)
    Empate
    >>> puntuaciones
    [0, 0]

    >>> puntuaciones = [0, 0]
    >>> comparar_jugadas('piedra', 'papel', puntuaciones)
    Gana Piedra
    >>> puntuaciones
    [1, 0]
    >>> puntuaciones = [0, 0]
    >>> comparar_jugadas('tijera', 'papel', puntuaciones)
    Gana Tijera
    >>> puntuaciones
    [1, 0]
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



if __name__ == "__main__":
    doctest.testmod()
