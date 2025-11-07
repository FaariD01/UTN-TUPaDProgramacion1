"""
Archivos - Práctica 
Objetivo: 
Comprender y aplicar el uso de archivos de texto en Python, desarrollando un 
pequeño programa que lea, procese y almacene información sobre productos de 
manera persistente. Se busca que el estudiante manipule datos a través de 
estructuras como listas y diccionarios, integrando lectura, escritura y buenas prácticas 
con archivos. 
"""
"""
Actividades: 
1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad
"""
import os

carpeta = "Unidad_8_Manejo_de_Archivos"

ruta_archivo = os.path.join(carpeta, "productos.txt")

with open(ruta_archivo, "w") as archivo:
    archivo.write("Shampoo,1500,20\n")
    archivo.write("Acondicionador,1800,15\n")
    archivo.write("Gel,1200,10\n")

print(f"Archivo creado en: {os.path.abspath(ruta_archivo)}")