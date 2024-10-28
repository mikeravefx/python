import random

def jugar_ronda(usuario, ordenador):
    if usuario == ordenador:
        return "Empate"
    elif (usuario == "piedra" and ordenador == "tijeras") or \
         (usuario == "tijeras" and ordenador == "papel") or \
         (usuario == "papel" and ordenador == "piedra"):
        return "Usuario"
    else:
        return "Ordenador"

def eleccion_ordenador(trampa, ultima_eleccion_usuario):
    if trampa:
        if ultima_eleccion_usuario == "piedra":
            return "papel"
        elif ultima_eleccion_usuario == "papel":
            return "tijeras"
        else:
            return "piedra"
    else:
        return random.choice(["piedra", "papel", "tijeras"])

def jugar():
    puntuacion_usuario = 0
    puntuacion_ordenador = 0
    trampa = False

    while puntuacion_usuario < 3 and puntuacion_ordenador < 3:
        usuario = input("Elige piedra, papel o tijeras: ").lower()
        ultima_eleccion_usuario = usuario
        ordenador = eleccion_ordenador(trampa, ultima_eleccion_usuario)
        
        ganador = jugar_ronda(usuario, ordenador)
        
        if ganador == "Usuario":
            puntuacion_usuario += 1
            print(f"Ganaste esta ronda. {usuario} vence a {ordenador}.")
        elif ganador == "Ordenador":
            puntuacion_ordenador += 1
            print(f"Perdiste esta ronda. {ordenador} vence a {usuario}.")
        else:
            print("Empate en esta ronda.")

        print(f"Puntuación: Usuario {puntuacion_usuario} - Ordenador {puntuacion_ordenador}")

        if puntuacion_usuario > puntuacion_ordenador:
            trampa = False
        else:
            trampa = True

    if puntuacion_usuario == 3:
        print("¡Felicidades! Ganaste la partida.")
    else:
        print("El ordenador ganó la partida.")

    repetir = input("¿Quieres volver a jugar? (s/n): ").lower()
    if repetir == 's':
        jugar()
    else:
        print("¡Gracias por jugar!")

if __name__ == "__main__":
    jugar()
