#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = float(input("Ingrese un numero:" ))

print(f"La tabla de multiplicar del {num} es: ")

for i in range(1, 11):
    print(f'{num} por {i}= ',num*i)