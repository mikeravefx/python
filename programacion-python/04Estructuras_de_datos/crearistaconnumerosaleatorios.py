import random
filas = 6
columnas = 7
min=0
max=100

listota2 = [[random.randint(min,max) for i in range(filas)] for j in range(columnas)] #para crear la matriz con número aleatorios

print(listota2)

lista_pares = [listota2[i][j] for i in range(len(listota2)) for j in range(len(listota2[i])) if listota2[i][j] % 2 == 0]
lista_impares = [listota2[i][j] for i in range(len(listota2)) for j in range(len(listota2[i])) if listota2[i][j] % 2 != 0]

# recorre la lista i j y verifica los numeros pares de lista

pares= 0
impares=0

for i in range(len(listota2)):
    for j in range(len(listota2[i])):
        pares += 1
    else:
        impares +=1

print("Lista Pares", lista_pares)
print("Cuantos Pares", pares)
print()
print("Lista impares", lista_impares)
print("Cuantos impares", impares)
