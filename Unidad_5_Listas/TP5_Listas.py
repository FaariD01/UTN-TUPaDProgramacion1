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

"""

"""

3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista.

"""
import random

lista_numeros_random = [random.randint(1,10) for _ in range(15)]


##Crear una lista con los pares y otra con los impares.

pares = []
impares = []
for numero in lista_numeros_random:
    if numero % 2 == 0:
       pares.append(numero) 
    else:
        impares.append(numero)

##Mostrar cuántos números tiene cada lista.

print(f'Listado de pares {pares}')
print(f'Listado de impares {impares}')
