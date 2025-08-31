#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 


altura = float(input("Ingrese su altura en m: "))
peso = float(input("Ingrese su peso en kg: "))

imc = peso/(altura**2)

print(f"Su indice de masa corporal es: {imc}%")
