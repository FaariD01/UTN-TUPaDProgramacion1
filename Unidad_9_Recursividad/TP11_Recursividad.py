"""
Práctico 11: Aplicación de la Recursividad  
Objetivo: 
Comprender el uso de recursividad en problemas matemáticos simples. 
Resultados de aprendizaje: 
✓ Comprensión y aplicación de la recursividad: El estudiante será capaz de definir y 
comprender el concepto de recursividad, identificando los casos base y recursivos en 
una función recursiva. 
✓ Diseño y desarrollo de algoritmos recursivos: El estudiante será capaz de diseñar 
funciones recursivas para resolver problemas complejos, descomponiendo el problema 
en subproblemas más sencillos. 
✓ Resolución de problemas a través de la recursividad: El estudiante será capaz de aplicar 
la recursividad en la resolución de una variedad de problemas, como la búsqueda en 
estructuras de datos, el ordenamiento y la generación de estructuras combinatorias. 
"""

"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario 
"""
def factorial(n):
    if n == 0 or n == 1:   # Caso base
        return 1
    else:                  # Caso recursivo
        return n * factorial(n - 1)


# Programa principal
num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")


"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique. 
"""
def fibonacci(n):
    if n <= 1:             # Casos base
        return n
    else:                  # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)


# Programa principal
pos = int(input("Ingrese la posición hasta donde mostrar la serie de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(pos):
    print(fibonacci(i), end=" ")
