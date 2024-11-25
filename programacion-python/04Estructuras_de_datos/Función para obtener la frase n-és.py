# 2b) Función para obtener la frase n-ésima
def obtener_frase(texto: str, numero: int) -> str:
    """
    Esta función recibe un texto con frases separadas por puntos y un número entero.
    Devuelve la frase correspondiente al número, o "Feliz Navidad" si el número está fuera de rango.
    """
    frases = texto.split(".")  # Dividir el texto en frases por puntos
    try:
        return frases[numero].strip()  # Devolver la frase número 'numero', eliminando espacios extra
    except IndexError:
        return "Feliz Navidad"  # Si el número está fuera de rango, devolver "Feliz Navidad"

# Ejemplo de uso
texto = "Feliz Año Nuevo. З Різдвом Христовим. Boas festas. Feliz Navidad."
numero = 3
print(obtener_frase(texto, numero))  # Debería devolver "Boas festas"
