"""

1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.


def imprimir_hola_mundo():
    
    print("Hola Mundo")
    
imprimir_hola_mundo()

"""

"""

2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.



def saludar_usuario(nombre):
    
    
    
    print(f"Hola {nombre} !!")
    
saludar_usuario("Juan")   

"""

"""

3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.



def informacion_personal(nombre, apellido, edad, residencia):
    
    print(f"Hola!! Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")


informacion_personal("Juan","Martinez",30,"Buenos Aires")

"""

"""

4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro
y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.



def calcular_area_circulo(radio):
    return 3.14 * (radio**2)

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = int(input("Ingrese el radio..."))

print(f"Radio: {calcular_area_circulo(radio)}")
print(f"Perimetro: {calcular_perimetro_circulo(radio)}")


"""


"""

Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    
    return segundos / 3600

print(segundos_a_horas(3600))

"""

"""

Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.


def tabla_multiplicar(numero):
    
    print(f"Tabla de multiplicar del numero {numero}")
    
    
    for i in range(1,11):
        
        print(f"{numero} x {i}: {numero*i}")
        

numero = int(input("Ingrese un numero:  "))
tabla_multiplicar(numero)


"""

"""

7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos,
multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

"""

