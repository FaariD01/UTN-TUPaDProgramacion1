#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = float(input("Ingrese dos numeros disntos de 0: "))
num2 = float(input("Ingrese dos numeros disntos de 0: "))

print(f"El resultado de sumar {num1} + {num2} es: ", num1+num2)
print(f"El resultado de restar {num1} - {num2} es: ", num1-num2)
print(f"El resultado de multiplicar {num1} * {num2} es: ", num1*num2)
print(f"El resultado de dividir {num1} / {num2} es: ", num1/num2)