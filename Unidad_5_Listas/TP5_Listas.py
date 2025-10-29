"""

1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja

notasEstudiantes = [10,9,8,7,6,5,4,3,2,1]

i = 0

###Mostrar la lista completa

for i in range(0,10):
    print(f"El estudiante {i+1} saco {notasEstudiantes[i]}")
  

###Calcular y mostrar el promedio

i = 0
acum = 0

for i in range(0,10):
    acum = acum + notasEstudiantes[i]

promedio = acum/(i+1)

print(f"El promedio de todas las notas es {promedio}")


###Indicar la nota más alta y la más baja

min = notasEstudiantes[0]
max = notasEstudiantes[0]

for i in range(0,10):
    if notasEstudiantes[i] < min:
        min = notasEstudiantes[i]
    elif notasEstudiantes[i] > max:
        max = notasEstudiantes[i]
    
print(f"La nota maxima es {max}")
print(f"La nota minima es {min}")

"""