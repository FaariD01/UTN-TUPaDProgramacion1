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

"""

2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

"""

lista_productos = []
i = 0
for i in range(0,5):
    producto = input("Ingrese un producto:  ")
    lista_productos.append(producto)
    
##Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted()

print(sorted(lista_productos))

##Preguntar al usuario qué producto desea eliminar y actualizar la lista.

borrar = input("Que producto desea eliminar? Ingrese el nombre...")

if borrar in lista_productos:
    lista_productos.remove(borrar)
    print(f"el producto {borrar} fue eliminado")
else:
    print(f"El producto {borrar} no se encuentra en la lista")

print(f'Lista actualizada: ', lista_productos)
