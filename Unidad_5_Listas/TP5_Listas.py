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


listaNumerica = [ 1,2,3,4,5,6,7,8 ]

print(f'Lista original: ', listaNumerica)

listaNumerica = listaNumerica[-1:] + listaNumerica[:-1]

print(f'Lista modificada: ', listaNumerica)

"""

"""

7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.


temperaturas_semana = [
    [15, 25],  # Lunes
    [14, 24],  # Martes
    [13, 23],  # Miércoles
    [16, 26],  # Jueves
    [12, 22],  # Viernes
    [11, 21],  # Sábado
    [10, 20]   # Domingo
]

##Calcular el promedio de las mínimas y el de las máximas.
suma_min = 0
suma_max = 0

for temp in temperaturas_semana:
    suma_min += temp[0]
    suma_max += temp[1]
    
promedio_min = suma_min / len(temperaturas_semana)
promedio_max = suma_max / len(temperaturas_semana)

print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}°C")

##Mostrar en qué día se registró la mayor amplitud térmica.

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

mayor_amplitud = 0
dia_mayor_amplitud = ""

for i, temp in enumerate(temperaturas_semana):
    amplitud = temp[1] - temp[0]  # máxima - mínima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias[i]

print(f"El día con mayor amplitud térmica fue {dia_mayor_amplitud} con {mayor_amplitud}°C")

"""

"""

8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia.


notas = [
    [8, 7, 9],  # Estudiante 1
    [6, 9, 7],  # Estudiante 2
    [7, 8, 6],  # Estudiante 3
    [9, 5, 8],  # Estudiante 4
    [10, 7, 9]  # Estudiante 5
]


##Mostrar el promedio de cada estudiante.
for i, estudiante in enumerate(notas):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Promedio del estudiante {i+1}: {promedio:.2f}")

num_materias = len(notas[0])
num_estudiantes = len(notas)

##Mostrar el promedio de cada materia.
for j in range(num_materias):
    suma_materia = 0
    for i in range(num_estudiantes):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / num_estudiantes
    print(f"Promedio de la materia {j+1}: {promedio_materia:.2f}")

"""

"""

9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada.


# Tablero 3x3 inicializado con "-"
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()  # línea en blanco para separar

def jugar(tablero, jugador):
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingrese la fila (0-2): "))
            columna = int(input(f"Jugador {jugador}, ingrese la columna (0-2): "))
            if tablero[fila][columna] == "-":
                tablero[fila][columna] = jugador
                break
            else:
                print("La casilla ya está ocupada, elija otra.")
        except (ValueError, IndexError):
            print("Entrada inválida. Debe ser un número entre 0 y 2.")

mostrar_tablero(tablero)

# Jugadores alternando X y O
for turno in range(4):  # se puede ampliar a 9 para toda la partida
    jugador_actual = "X" if turno % 2 == 0 else "O"
    jugar(tablero, jugador_actual)
    mostrar_tablero(tablero)

"""

"""

10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.

"""

ventas = [
    [10, 12, 15, 11, 14, 13, 16],  # Producto 1
    [5, 8, 7, 6, 9, 10, 7],        # Producto 2
    [20, 18, 19, 21, 22, 20, 23],  # Producto 3
    [7, 9, 8, 6, 5, 10, 12]        # Producto 4
]

productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

##Mostrar el total vendido por cada producto.

for i, producto in enumerate(ventas):
    total = sum(producto)
    print(f"Total vendido del {productos[i]}: {total}")
    
##Mostrar el día con mayores ventas totales.
ventas_por_dia = [0]*7  # inicializa lista de 7 días

for j in range(7):  # recorrer columnas
    for i in range(4):  # recorrer productos
        ventas_por_dia[j] += ventas[i][j]

##Indicar cuál fue el producto más vendido en la semana.
max_ventas = max(ventas_por_dia)
indice_dia = ventas_por_dia.index(max_ventas)
print(f"El día con mayores ventas fue {dias[indice_dia]} con {max_ventas} ventas")


total_productos = [sum(fila) for fila in ventas]
max_total = max(total_productos)
indice_producto = total_productos.index(max_total)
print(f"El producto más vendido en la semana fue {productos[indice_producto]} con {max_total} unidades")


