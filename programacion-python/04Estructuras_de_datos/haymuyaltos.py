edad_media= 0
altura_media=0
mayores_edad=0
mas_altos=0
NUM_ALUMNOS=2
hay_muy_altos = False

for i in range(NUM_ALUMNOS):
    edad= int(input("Introduce la Edad del Alumno:"))
    altura = float(input("Introduce de altura del alumno:"))
edad_media+= edad
altura_media+=altura
media_edad =  edad_media/NUM_ALUMNOS
altura_media= altura_media/NUM_ALUMNOS

if edad>=18:
     mayores_edad += 1
if altura > 1.75:
     mas_altos += 1

if altura > 1.90:
     hay_muy_altos = True
print (round(edad,2), round(edad_media,2))
print (round(mayores_edad,2), round(mas_altos,2))

if hay_muy_altos == True:
     print("Hay algun alumno que mide mas de 1.90")