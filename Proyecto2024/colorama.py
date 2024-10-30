from colorama import init, Fore, Back, Style
import sys
import time

# Inicializar colorama
init(autoreset=True)

def imprimir_con_color(texto, color):
    print(color + texto)

def imprimir_con_blinking(texto):
    # Secuencia ANSI para hacer parpadear el texto
    blinking_text = '\033