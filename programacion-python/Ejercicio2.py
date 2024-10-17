# ## Ejercicio 2
# Crea un programa que pida el usuario la base y exponente de una potencia y calcule su resultado.
print("Introduzca la base de un numero para determinar la base N")
base = input()
base_int = int(base)
print("Introduzca la base de un numero para el Exponente")
exponente=input()
exponente_int=int(exponente)
Resultado= base_int ** exponente_int
print("El resultado de la base", base_int, "Cuyo exponente es ", exponente_int, " Es = A:", Resultado)
