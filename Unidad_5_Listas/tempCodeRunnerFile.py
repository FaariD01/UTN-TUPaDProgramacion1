#Indicar la nota más alta y la más baja

min = notasEstudiantes[0]
max = notasEstudiantes[0]

for i in range(0,10):
    if notasEstudiantes[i] < min:
        min = notasEstudiantes[i]
    elif notasEstudiantes[i] > max:
        max = notasEstudiantes[i]
    
print(max)
print(min)