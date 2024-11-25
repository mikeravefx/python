# 3a) Calcular los visitantes totales a cada atracción
def calcular_visitantes_totales(visitantes: list) -> list:
    """
    Esta función recibe una lista bidimensional de visitantes (donde cada sublista es una atracción)
    y devuelve una lista con los visitantes totales de cada atracción.
    """
    return [sum(atraccion) for atraccion in visitantes]

# Ejemplo de uso
visitantes = [
    [1500, 1600, 1700, 1800, 1900],  # visitas al árbol
    [2000, 2100, 2200, 2300, 2400],  # visitas a la bola
    [1800, 1900, 2000, 2100, 2200],  # visitas al muñeco
    [1700, 1600, 1800, 1900, 1494]   # visitas a la noria
]
totales = calcular_visitantes_totales(visitantes)
for i, total in enumerate(totales):
    print(f"Los visitantes totales de la atracción {i+1} fueron {total}")


# # 3b) Determinar la atracción más visitada
def atraccion_mas_visitada(totales: list, atracciones: list) -> str:
    """
    Esta función recibe la lista de totales de visitantes y la lista de atracciones,
    y devuelve el nombre de la atracción más visitada.
    """
    max_visitas = max(totales)
    indice = totales.index(max_visitas)
    return atracciones[indice]

# Ejemplo de uso
atracciones = ["árbol", "bola", "muñeco", "noria"]
print("La atracción más visitada fue", atraccion_mas_visitada(totales, atracciones))


# # 3c) Buscar qué día y atracción tuvo más visitantes
def dia_con_mas_visitantes(visitantes: list, atracciones: list) -> str:
    """
    Esta función recibe la lista bidimensional de visitantes y la lista de atracciones,
    y devuelve el día y la atracción que tuvieron más visitantes.
    """
    max_visitantes = 0
    atraccion_max = ""
    dia_max = 0

    for i, atraccion in enumerate(visitantes):
        for j, visitantes_dia in enumerate(atraccion):
            if visitantes_dia > max_visitantes:
                max_visitantes = visitantes_dia
                atraccion_max = atracciones[i]
                dia_max = j + 1  # Día numerado desde 1

    return f"El mayor número de visitantes se produjo en {atraccion_max}, el día {dia_max}º, con {max_visitantes} visitantes."

# Ejemplo de uso
print(dia_con_mas_visitantes(visitantes, atracciones))
