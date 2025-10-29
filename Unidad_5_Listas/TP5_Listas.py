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

"""
"""
4) Dada una lista con valores repetidos:
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.




datos = [1,3,5,3,7,1,9,5,3]

datos_sin_repetidos = list(set(datos))

print(datos_sin_repetidos)

"""

"""

5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.


estudiantes_presentes = ["Farid", "Juan", "Mariana", "Yamil", "Valentina", "Agustin", "Rodrigo", "Daniela"]

print(f'Estudiantes presentes {estudiantes_presentes}')

##• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.

eliminar_o_agregar = input("Desea agregar o eliminar algun estudiante? Indique A o E: ")

if eliminar_o_agregar == "E":
    estudiante = input("A quien desea eliminar? ")
    if estudiante in estudiantes_presentes:
        estudiantes_presentes.remove(estudiante)
    else:
        print("El estudiante no esta en la lista")
else:
    nuevoEstudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes_presentes.append(nuevoEstudiante)

##Mostrar la lista final actualizada.
print(f'Lista actualizada: ', estudiantes_presentes)

"""

"""

6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).

"""

listaNumerica = [ 1,2,3,4,5,6,7,8 ]

print(f'Lista original: ', listaNumerica)

listaNumerica = listaNumerica[-1:] + listaNumerica[:-1]

print(f'Lista modificada: ', listaNumerica)