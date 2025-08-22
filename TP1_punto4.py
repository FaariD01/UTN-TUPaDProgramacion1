#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

radio = float(input("Ingrese el radio: "))

pi = 3.1416

area = pi * radio**2
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")