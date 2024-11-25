# 2a) Función para comparar si dos cadenas son parecidas
def son_cadenas_parecidas(cadena1: str, cadena2: str = "Feliz Navidad") -> bool:
    """
    Esta función compara dos cadenas y devuelve True si son parecidas según el criterio especificado:
    - Las dos deben tener la misma longitud.
    - Las dos primeras y dos últimas letras deben coincidir, sin importar mayúsculas y minúsculas.
    """
    # Convertimos ambas cadenas a minúsculas para que no importe la mayúscula/minúscula
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()

    if len(cadena1) == len(cadena2):
        # Comprobamos las primeras y últimas dos letras
        return cadena1[:2] == cadena2[:2] and cadena1[-2:] == cadena2[-2:]
    return False

# Ejemplo de uso
resultado = son_cadenas_parecidas("Una casa", "Uno pasa")
print(resultado)  # Debería devolver True
