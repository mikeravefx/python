# Crea un programa en Python que:
# Pida al usuario su peso y lo guarde en una variable

# Defina una constante con el valor de KG por libra

# Calcule el peso en libras

# Muestre por pantalla el peso en libras

KILO = 2.20462262
UNKilo_f = float(KILO)
print("Introduzca su Peso")
peso= input()
peso_f=float(peso)
# Si UNKilo_f=2,20462262 peso cuanto sera
total=(peso_f/UNKilo_f)
print("Su peso en libras es: ", round(total,2))