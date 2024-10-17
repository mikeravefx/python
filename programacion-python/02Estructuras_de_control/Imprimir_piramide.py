def dibujar_escalera(filas):
    for i in range(1, filas + 1):
        # Espacios en blanco
        for j in range(filas - i):
            print(" ", end="")
        # Números descendentes
        for j in range(i, 0, -1):
            print(j, end="")
        # Números ascendentes
        for j in range(2, i + 1):
            print(j, end="")
        # Nueva línea
        print()

# Solicitar al usuario el número de filas
filas = int(input("Introduce el número de filas: "))
dibujar_escalera(filas)