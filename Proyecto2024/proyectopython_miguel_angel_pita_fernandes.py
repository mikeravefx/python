import random
import time
import sys
import os

# Variables globales para acumular las victorias
victorias_ordenador = 0
victorias_usuario = 0

# Lista para almacenar las estadísticas
estadisticas = [victorias_ordenador, victorias_usuario]

# Imprimir texto con delay
def imprimir_texto_dinamico(texto, delay=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Nueva línea al final del texto

# Borrar Pantalla
def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Mostrar tabla ASCII
def mostrar_tabla(titulo, contenido):
    """Muestra una tabla con bordes ASCII."""
    longitud_maxima = max(len(linea) for linea in contenido)
    borde_horizontal = '*' + '=' * (longitud_maxima + 2) + '*'
    
    print(borde_horizontal)
    print(f"| {titulo.center(longitud_maxima)} |")
    print(borde_horizontal)
    for linea in contenido:
        print(f"| {linea.ljust(longitud_maxima)} |")
    print(borde_horizontal)

# Obtiene jugada del jugador como entero, en donde se devuelve la opción entera de la elección del usuario.
def obtener_jugada_ordenador(jugada_jugador: int, modo_trampa: bool) -> int:
    """Devuelve la jugada que el ordenador debe elegir. En modo trampa, siempre elige la que gana."""
    if modo_trampa:
        return {1: 2, 2: 3, 3: 1}[jugada_jugador]
    return random.choice([1, 2, 3])

# Compara las jugadas entre el ordenador y el jugador y devuelve una tupla con los resultados
def comparar_jugadas(jugada_jugador: int, jugada_ordenador: int) -> tuple:
    """Compara las jugadas del jugador y el ordenador, y retorna las puntuaciones actualizadas."""
    if jugada_jugador == jugada_ordenador:
        mostrar_tabla("Resultado", ["Empate"])
        return 0, 0
    elif (jugada_jugador == 1 and jugada_ordenador == 3) or \
         (jugada_jugador == 3 and jugada_ordenador == 2) or \
         (jugada_jugador == 2 and jugada_ordenador == 1):
        mostrar_tabla("Resultado", ["Ganaste esta ronda."])
        return 1, 0
    else:
        mostrar_tabla("Resultado", ["Perdiste esta ronda."])
        return 0, 1


# Jugar una partida
def jugar(modo_trampa: bool) -> None:
    global victorias_ordenador, victorias_usuario, estadisticas
    borrar_pantalla()
    puntuacion_usuario = 0
    puntuacion_ordenador = 0
    activartrampa = False 

    while puntuacion_usuario < 3 and puntuacion_ordenador < 3:
        mostrar_tabla('Opciones', ['1. Piedra', '2. Papel', '3. Tijeras'])

        try:
            eleccion = int(input("Tu elección (1-3): "))
            if eleccion not in [1, 2, 3]:
                raise ValueError("Opción no válida")
            borrar_pantalla()
        except ValueError as e:
            print(e)
            continue

        jugada_jugador = eleccion
        jugada_ordenador = obtener_jugada_ordenador(jugada_jugador, activartrampa)

        if modo_trampa and puntuacion_usuario == 2:
            activartrampa = True
            jugada_ordenador = obtener_jugada_ordenador(jugada_jugador, modo_trampa)
            imprimir_texto_dinamico("¡Oh no! El ordenador está trampeando... ¡Escojo mi jugada!")
        else:
            opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
            mostrar_tabla("Elecciones", [f"Tú elegiste: {opciones[jugada_jugador]}", f"Ordenador eligió: {opciones[jugada_ordenador]}"])

        puntuacion_usuario_ronda, puntuacion_ordenador_ronda = comparar_jugadas(jugada_jugador, jugada_ordenador)
        puntuacion_usuario += puntuacion_usuario_ronda
        puntuacion_ordenador += puntuacion_ordenador_ronda

        mostrar_tabla("Puntuación", [f"Usuario: {puntuacion_usuario}", f"Ordenador: {puntuacion_ordenador}"])

    if puntuacion_usuario == 3:
        imprimir_texto_dinamico("¡Felicidades! Ganaste la partida.")
        victorias_usuario += 1
    else:
        imprimir_texto_dinamico("El ordenador ganó la partida. ¡Mejor suerte la próxima vez!")
        victorias_ordenador += 1

    # Actualizamos la lista de estadísticas
    estadisticas[0], estadisticas[1] = victorias_ordenador, victorias_usuario

    mostrar_tabla("Resultados", [f"Puntuación total: Usuario {puntuacion_usuario}, Ordenador {puntuacion_ordenador}",
                                 f"Victorias totales - Ordenador: {victorias_ordenador}, Usuario: {victorias_usuario}"])

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
            borrar_pantalla()
            mostrar_tabla('Instrucciones', ['1. Piedra vence a tijeras', '2. Papel vence a piedra', '3. Tijeras vence a papel',
                                            'Elige tu opción y compite contra el ordenador. El primer jugador en ganar 3 rondas es el vencedor.'])
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
            mostrar_tabla('Gracias por jugar', ['¡Hasta luego!'])
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    # Ejecutar programa principal
programaprincipal()
