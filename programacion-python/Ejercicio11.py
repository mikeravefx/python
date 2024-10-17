horas_comienzo = int(input("Indica la hora de inicio:"))
minutos_comienzo = int(input("Indica los minutos de comienzo:"))
duracion = int(input("Indica la duracion en minutos:"))

minutos_totais = minutos_comienzo +duracion
minutos_resultado = minutos_totais % 60
horas_resultado = horas_comienzo + minutos_totais // 60

print(horas_resultado, minutos_resultado, sep=":")