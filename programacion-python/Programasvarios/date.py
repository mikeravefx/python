import datetime
x = datetime.datetime.now()
print(x)

from datetime import datetime, timedelta

# Definir los tiempos que quieres sumar
tiempo1 = datetime.now()
tiempo2 = timedelta(hours=1, minutes=30, seconds=10)

# Sumar los tiempos
nuevo_tiempo = tiempo1 + tiempo2

print(nuevo_tiempo)

# Utilizando la duncion tiempo

from datetime import date, timedelta
 
current_date = date.today()
 
print("Fecha de Hoy : ",current_date)
 
print("Fecha mas 1 dias: ",current_date - timedelta(1))


