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

6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. 

"""
"""


i = 100

for i in range (101,0,-1):
    if i%2 == 0:
        print(i)
    else: 
        continue

"""

"""

7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario.

"""

"""

i = 0 
acum = 0 

num = int(input("Ingrese un numero entero positivo: "))

for i in range ( 0, num+1):
    acum += i
    
    
print(f'La suma de los numeros es {acum}')

"""

"""

8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

"""

"""

i = 0

nPares = 0
nImpares = 0
nNegativos = 0
nPostivos = 0



while (i < 101):
    num = int(input("Ingrese un numero: "))
    
    if num % 2 == 0:
        nPares += 1
    else:
        nImpares += 1
        
    if num < 0:
        nNegativos += 1
    else: 
        nPostivos += 1

    i += 1
    

print(f'Cantidad de numeros pares: {nPares}')
print(f'Cantidad de numeros impares: {nImpares}')
print(f'Cantidad de numeros negativos: {nNegativos}')
print(f'Cantidad de numeros positivos: {nPostivos}')

"""

"""

9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). 

"""
"""

i = 0
acum = 0



while (i < 101):
    num = int(input("Ingrese un numero: "))
    acum += num
    i += 1

print(f'La media entre {acum} / {i} es: {acum/i}')

"""