# Función para calcular el promedio de temperaturas de cada mes
def calcular_promedio_temperaturas(tabla_temperaturas):
    # Crear un diccionario vacío donde almacenaremos los promedios
    promedios = {}
    
    # Recorrer cada mes en la tabla_temperaturas
    for mes, temperaturas in tabla_temperaturas.items():
        # Sumar todas las temperaturas de ese mes
        suma_temperaturas = 0
        for temperatura in temperaturas:
            suma_temperaturas += temperatura
        
        # Calcular el promedio dividiendo la suma de las temperaturas entre la cantidad de días
        promedio = suma_temperaturas / len(temperaturas)
        
        # Almacenar el promedio en el diccionario promedios
        promedios[mes] = promedio
    
    return promedios

# Función para recorrer y mostrar las temperaturas de cada mes
def mostrar_temperaturas(tabla_temperaturas):
    # Recorrer la tabla_temperaturas para mostrar las temperaturas mes a mes
    for mes, temperaturas in tabla_temperaturas.items():
        print(f"Temperaturas de {mes}: {temperaturas}")

# Tabla de temperaturas predefinidas (como en el ejemplo anterior)
tabla_temperaturas = {
    'Enero': [5, 6, 7, 5, 4, 5, 6, 6, 7, 6, 5, 6, 5, 4, 5, 6, 6, 7, 8, 7, 6, 5, 6, 5, 4, 3, 4, 5, 6, 7, 8],
    'Febrero': [6, 7, 8, 7, 6, 7, 6, 6, 7, 6, 7, 6, 7, 7, 6, 7, 8, 7, 6, 5, 6, 6, 5, 6, 7, 6, 6, 5],
    'Marzo': [10, 11, 12, 13, 12, 11, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
    'Abril': [15, 16, 15, 14, 15, 16, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 16, 15, 14, 13, 14],
    'Mayo': [20, 21, 22, 23, 24, 23, 22, 21, 20, 21, 22, 23, 24, 25, 24, 23, 22, 21, 20, 21, 22, 23, 24, 25, 26, 25, 24, 23, 22, 21, 20],
    'Junio': [25, 26, 27, 28, 27, 26, 25, 24, 25, 26, 27, 28, 29, 28, 27, 26, 25, 24, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26],
    'Julio': [30, 31, 30, 29, 30, 31, 32, 31, 30, 29, 30, 31, 32, 31, 30, 29, 30, 31, 32, 33, 32, 31, 30, 29, 28, 29, 30, 31, 32, 33, 32],
    'Agosto': [29, 30, 31, 30, 29, 28, 29, 30, 31, 32, 31, 30, 29, 30, 31, 32, 33, 32, 31, 30, 29, 28, 29, 30, 31, 32, 31, 30, 29, 28, 29],
    'Septiembre': [25, 24, 23, 24, 25, 26, 27, 26, 25, 24, 23, 24, 25, 26, 27, 28, 27, 26, 25, 24, 23, 24, 25, 26, 27, 26, 25, 24, 23, 24],
    'Octubre': [15, 16, 17, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15, 14, 13, 12, 13, 14, 15, 16, 17, 18, 19, 18, 17],
    'Noviembre': [8, 9, 10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 6, 7, 8, 9],
    'Diciembre': [5, 6, 7, 6, 5, 4, 5, 6, 7, 6, 5, 4, 3, 4, 5, 6, 7, 6, 5, 4, 3, 4, 5, 6, 7, 6, 5, 4, 3, 4, 5]
}

# Llamar a las funciones
mostrar_temperaturas(tabla_temperaturas)  # Muestra las temperaturas de cada mes
promedios = calcular_promedio_temperaturas(tabla_temperaturas)  # Calcula los promedios

# Mostrar los promedios
print("\nPromedios mensuales de temperatura:")
for mes, promedio in promedios.items():
    print(f"{mes}: {promedio:.2f} °C")
