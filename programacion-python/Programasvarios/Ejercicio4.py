# Crea un programa en Python que:

# Pida al usuario su nombre y lo guarde en una variable

# pida al usuario su peso y lo guarde en una variable

# pida al usuario su altura (en m) y lo guarde en una variable

# Calcule el IMC (peso / altura^2) (Índice de masa corporal)

# Muestre por pantalla el nombre y el IMC
print("Introduzca su nombre")
nombre = input()
print("Introduzca su Peso")
peso= input()
peso_f= float(peso)
print("Introduzca su Altura")
altura= input()
altura_f= float(altura)
IMC= (peso_f / altura_f ** 2)
round(IMC,2)
print("Su nombrees:", nombre, "Su peso es:", peso_f, "Su Altua es:", altura_f, "El resultado de Su IMC es", round(IMC,2))