"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

"""
"""
i = 1

for i in range(1,100):
    if i%2 == 0:
        print(i)
        i+=1
    else:
        i+=1
        
"""

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.

"""

"""
i = 1
num = int(input("Ingrese un numero: "))

while ( num % 10 < 1 ):
    num = num / 10
    i+=1

print(f'El numero ingresado tiene {i} digitos')

"""

"""

3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.

"""
"""

num1 = int(input("Ingrese el valor minimo: "))
num2 = int(input("Ingrese el valor maximo: "))

i = num1
suma = 0
for i in range(num1+1,num2):
    suma += i

print(f'{suma}')

"""

"""

4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.

"""

"""
acum = 0
i = 0

i = int(input("Ingrese un numero: ")) 

while i != 0:
    
    acum += i
    i = int(input("Ingrese un numero: ")) 

print(f'La suma de los numeros ingresados es {acum}')

"""

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

"""

"""

i = 1
numAleatorio = 4

numControl = int(input("Adivine el numero entre 0 y 9: "))

while numAleatorio != numControl:
    if 0 <= numControl <= 9:
        i+=1
        numControl = int(input("Adivine el numero entre 0 y 9: "))
    else:
        print("Error ingreso un numero por fuera de los limites")
        numControl = int(input("Adivine el numero entre 0 y 9: "))
        

print(f'Intentos para adivinar {i}')

"""


"""

"""