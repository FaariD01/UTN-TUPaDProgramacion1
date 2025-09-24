i = 1
numAleatorio = 4

numControl = int(input("Adivine el numero entre 0 y 9: "))

while numAleatorio != numControl:
    if numControl >= 0 and numControl <= 9:
        i+=1
        numControl = int(input("Adivine el numero entre 0 y 9: "))
    else:
        print("Error ingreso un numero por fuera de los limites")
        numControl = int(input("Adivine el numero entre 0 y 9: "))
        

print(f'Intentos para adivinar {i}')