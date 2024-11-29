def es_verbo(palabra: str) -> bool:
    """
    Determina si una palabra es un verbo en español, basándose en su terminación.
    
    Un verbo en español suele terminar en 'ar', 'er', o 'ir'. Esta función verifica si la
    palabra dada termina con alguno de estos sufijos para considerarla un verbo.

    Args:
        palabra (str): La palabra a verificar.

    Returns:
        bool: `True` si la palabra termina en 'ar', 'er' o 'ir', `False` en caso contrario.
    
    Ejemplos:
    >>> es_verbo("cantar")
    True
    >>> es_verbo("comer")
    True
    >>> es_verbo("vivir")
    True
    >>> es_verbo("casa")
    False
    >>> es_verbo("agua")
    False
    """
    if palabra.endswith('ar') or palabra.endswith('er') or palabra.endswith('ir'):
        return True
    else:
        return False
