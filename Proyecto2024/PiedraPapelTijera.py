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
        # Verificar el sistema operativo y ejecutar el comando adecuado 
    if os.name == 'nt': # Para Windows 
        os.system('cls') 
    else: # Para Linux y macOS 
     os.system('clear')
     
def jugar(opciones:int)->str:
    opciones = ["piedra", "papel", "tijeras"]
    puntuacion_usuario = 0
    puntuacion_ordenador = 0

    while puntuacion_usuario < 3 and puntuacion_ordenador < 3:
        imprimir_texto_dinamico('''\nElige una opción:\n"1. Piedra"\n"2. Papel"\n"3. Tijeras''',delay= 0.00001)
        eleccion = int(input("Tu elección: "))
        jugada_jugador = opciones[eleccion - 1]
        jugada_ordenador = random.choice(opciones)
        borrar_pantalla()
        
        print("Tú elegiste:", jugada_jugador)
        print("Ordenador eligió: ",jugada_ordenador)
        
       
        if jugada_jugador == jugada_ordenador:
            imprimir_texto_dinamico("Empate")

        elif (jugada_jugador == "piedra" and jugada_ordenador == "tijeras") or \
             (jugada_jugador == "tijeras" and jugada_ordenador == "papel") or \
             (jugada_jugador == "papel" and jugada_ordenador == "piedra"):
            puntuacion_usuario += 1
            imprimir_texto_dinamico(print("Ganaste esta ronda."),delay=0.02)           
            borrar_pantalla() 
          
        else:
            puntuacion_ordenador += 1
            imprimir_texto_dinamico("Perdiste esta ronda.",delay=0.02)
            

        print("Puntuación: Usuario", puntuacion_usuario,"- Ordenador ", puntuacion_ordenador)
        time.sleep(2)
        borrar_pantalla() 
       
    if puntuacion_usuario == 3:
       
        imprimir_texto_dinamico("¡Felicidades! Ganaste la partida.",delay=0.02)
    else:
        
        imprimir_texto_dinamico("El ordenador ganó la partida.",delay=0.02)



def programaprincipal():
    while True:
        # mostrar_menu()
        borrar_pantalla() 
        imprimir_texto_dinamico('''"Menú:"\n"1. Jugar"\n"2. Ver instrucciones"\n"3. Salir"''',0.05)
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            jugar(opcion)
            
        elif opcion == 2:
            borrar_pantalla() 
            imprimir_texto_dinamico('''"\nInstrucciones:"\n"1. Piedra vence a tijeras"
                            \n"2. Papel vence a piedra"
                            \n"3. Tijeras vence a papel"
                            \n"Elige tu opción y compite contra el ordenador.El primer jugador en ganar 3 rondas es el vencedor.\n"''',delay=0.0001)
        elif opcion == 3:
            imprimir_texto_dinamico("Gracias por jugar. ¡Hasta luego!",delay=0.0001)
            
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            break
        # Ejecutar programa Principal.

programaprincipal()
