def es_primo (numero: int) -> bool:
    primo = True
    for i in range (2, numero):
         if numero %i == 0:
              return False
    return True     

numero = int(input("Dime un numero: "))
for i in range (1,numero):
    
    if es_primo(i):
        print(i, "Es Primo")
    else:
         print("No es primo")
     
# Imprimir PiramideS de Derecha a izquierda

def piramide(numero:int )-> None:
    for i in range(1, numero + 1):
         # filas
        for j  in range(i,0,-1): 
               #Columnas 
               print(j, end="")
        print()


piramide(5)  

# Imprimir PiramideS de Izquierda a derecha

def piramide1(altura:int )-> None:
    for fila in range(1, altura + 1): #  FILAS
        print(" "  * (altura-fila),end="")
        for columna in range(fila,0,-1):  #Columnas 
            print(columna, end="")
        print()

piramide1(5)  

# Imprimir PiramideS de Como Arbolito de Navidad

def piramide2(altura:int )-> None:
    for fila in range(1, altura + 1): #  FILAS
        print(" "  * (altura-fila),end="")         
        for columna in range(fila,0,-1): #Espacios iniciales
            print(columna, end="")   #Columnas 1 primera parte
        for columna in range(2,fila+1):
            print(columna, end="")  #Columna segunda parte
        print()

piramide2(5) 