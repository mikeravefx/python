import random

# Definir el tamaño de la matriz 3D
filas = 6
columnas = 7
capas = 4  # Número de capas en la matriz 3D
min = 0
max = 100

# Crear la matriz 3D con números aleatorios
matriz_3d = [[[random.randint(min, max) for i in range(columnas)] for j in range(filas)] for k in range(capas)]

# Mostrar la matriz 3D
for capa in range(capas):
    print(f"Capa {capa+1}:")
    for fila in range(filas):
        print(matriz_3d[capa][fila])

# Inicializar listas para pares e impares
lista_pares = []
lista_impares = []

# Recorrer la matriz 3D y separar los números pares e impares
for capa in range(capas):
    for fila in range(filas):
        for col in range(columnas):
            if matriz_3d[capa][fila][col] % 2 == 0:
                lista_pares.append(matriz_3d[capa][fila][col])
            else:
                lista_impares.append(matriz_3d[capa][fila][col])

# Contar cuántos números pares e impares
pares = len(lista_pares)
impares = len(lista_impares)

# Mostrar los resultados
print("\nLista de Pares:", lista_pares)
print("Cantidad de Pares:", pares)
print()
print("Lista de Impares:", lista_impares)
print("Cantidad de Impares:", impares)
