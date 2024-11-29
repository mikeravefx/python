cadena="hola como estas"

def devover(cadena: str) -> bool:
    resultado=""
    for letra in cadena:
        if not letra.isspace() and letra.isalpha():
            resultado += letra
        return True
    
    else:
        return False
    
"""
>>> devolver('hola como estas')
    True
"""