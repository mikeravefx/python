import random
import time
import sys


def imprimir_texto_dinamico(texto, delay=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Nueva línea al final del texto

  
def mostrar_menu():
    imprimir_texto_dinamico('''"Menú:"\n"1. Jugar"\n"2. Ver instrucciones"\n"3. Salir"''',0.05)

def ver_instrucciones():
    print("\nInstrucciones:")
    print("1. Piedra vence a tijeras")
    print("2. Papel vence a piedra")
    print("3. Tijeras vence a papel")
    print("Elige tu opción y compite contra el ordenador. El primer jugador en ganar 3 rondas es el vencedor.\n")

def jugar():
    opciones = ["piedra", "papel", "tijeras"]
    puntuacion_usuario = 0
    puntuacion_ordenador = 0

    while puntuacion_usuario < 3 and puntuacion_ordenador < 3:
        print('''\nElige una opción:\n"1. Piedra"\n"2. Papel"\n"3. Tijeras''')
        eleccion = int(input("Tu elección: "))
        jugada_jugador = opciones[eleccion - 1]
        jugada_ordenador = random.choice(opciones)
        
        print("Tú elegiste:", jugada_jugador)
        print("Ordenador eligió: ",jugada_ordenador)

        
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

        print("Puntuación: Usuario", puntuacion_usuario,"- Ordenador ", puntuacion_ordenador)

    if puntuacion_usuario == 3:
        print("¡Felicidades! Ganaste la partida.")
    else:
        print("El ordenador ganó la partida.")



def menu():
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            jugar()
        elif opcion == 2:
            ver_instrucciones()
        elif opcion == 3:
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
menu()