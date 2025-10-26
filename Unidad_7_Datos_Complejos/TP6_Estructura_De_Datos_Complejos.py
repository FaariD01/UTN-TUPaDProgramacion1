"""

1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 

"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)



"""

2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800

"""

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

"""

3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. 

"""

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

"""

4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe.

"""
"""
agenda = {}

for i in range(2):
    nombre = input(f'Ingresa el nombre del contacto {i+1}: ')
    numero = int(input(f"Ingresa el numero de {nombre}: "))
    agenda[nombre] = numero
    
nombre_buscar = input("Ingresa el nombre a consultar: ")

if nombre_buscar in agenda:
    print(f"El numero de {nombre_buscar} es: {agenda[nombre_buscar]}")
else:
    print(f"No se encontro un contacto con el nombre {nombre_buscar}")
"""  
    
"""

5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra.


"""

"""
frase = input("Ingresa una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

print("Palabras unicas:", palabras_unicas)

conteo_de_palabras = {}

for palabra in palabras:
    if palabra in conteo_de_palabras:
        conteo_de_palabras[palabra] += 1
    else:
     conteo_de_palabras[palabra] = 1



print("Cantidad de veces que aparece cada palabra:", conteo_de_palabras )


"""
"""

alumnos = {}

for i in range(3):
    nombre_alumno = input("Ingres el nombre del alumno: ")
    nota_alumno = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1} de {nombre_alumno}: "))
        nota_alumno.append(nota)
    alumnos[nombre_alumno]= tuple(nota_alumno)

print("\nAlumnos y sus notas:")
for nombre_alumno, nota_alumno in alumnos.items():
    print(f"{nombre_alumno}: {nota_alumno}")
"""


"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

"""


parcial1 = {"Ana", "Luis", "María", "Jorge", "Carla"}
parcial2 = {"María", "Jorge", "Sofía", "Pedro"}


ambos = parcial1 & parcial2   
print("Aprobaron ambos parciales:", ambos)


solo_uno = parcial1 ^ parcial2  
print("Aprobaron solo uno de los dos:", solo_uno)


al_menos_uno = parcial1 | parcial2 
print("Aprobaron al menos un parcial:", al_menos_uno)
