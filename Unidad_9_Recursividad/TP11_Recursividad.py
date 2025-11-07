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

"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
algoritmo general. 
"""

def potencia(base, exponente):
    if exponente == 0:     # Caso base
        return 1
    else:                  # Caso recursivo
        return base * potencia(base, exponente - 1)


# Programa principal
b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))

print(f"{b}^{e} = {potencia(b, e)}")

"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto. 

"""

def decimal_a_binario(n):
    if n == 0:             # Caso base
        return ""
    else:                  # Caso recursivo
        return decimal_a_binario(n // 2) + str(n % 2)


# Programa principal
num = int(input("Ingrese un número entero positivo: "))

# Si el número es 0, el resultado debe ser "0"
resultado = decimal_a_binario(num)
if resultado == "":
    resultado = "0"

print(f"El número {num} en binario es: {resultado}")

"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es. 
     Requisitos: 
La solución debe ser recursiva. 
No se debe usar [::-1] ni la función reversed().
"""
def es_palindromo(palabra):
    if len(palabra) <= 1:       # Caso base
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:                       # Caso recursivo
        return es_palindromo(palabra[1:-1])


# Programa principal
texto = input("Ingrese una palabra: ").lower()
if es_palindromo(texto):
    print("Es un palíndromo ")
else:
    print("No es un palíndromo ")

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
número entero positivo y devuelva la suma de todos sus dígitos. 
     Restricciones: 
No se puede convertir el número a string. 
Usá operaciones matemáticas (%, //) y recursión. 
Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5)
"""

def suma_digitos(n):
    if n < 10:              # Caso base
        return n
    else:                   # Caso recursivo
        return (n % 10) + suma_digitos(n // 10)


# Programa principal
num = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")

"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 
 
      Ejemplos: 
contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
"""

def contar_bloques(n):
    if n == 1:              # Caso base
        return 1
    else:                   # Caso recursivo
        return n + contar_bloques(n - 1)


# Programa principal
niveles = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")


"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
aparece ese dígito dentro del número. 
      Ejemplos: 
contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4
"""

def contar_digito(numero, digito):
    if numero == 0:         # Caso base
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


# Programa principal
num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a contar (0-9): "))

print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}.")
