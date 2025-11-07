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

with open("Unidad_8_Manejo_de_Archivos/productos.txt", "w") as archivo:
    archivo.write("Shampoo,1500,20\n")
    archivo.write("Acondicionador,1800,15\n")
    archivo.write("Gel,1200,10\n")

print(f"Archivo creado")

"""
2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: 
"""

with open("Unidad_8_Manejo_de_Archivos/productos.txt", "r") as archivo:
    print("Listado de productos:\n")
    
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
            
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

"""
3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""


with open("Unidad_8_Manejo_de_Archivos/productos.txt", "r") as archivo:
    print("Listado de productos:\n")

    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\n--- Agregar nuevo producto ---")
nombre_nuevo = input("Nombre del producto: ")
precio_nuevo = input("Precio: ")
cantidad_nueva = input("Cantidad: ")

with open("Unidad_8_Manejo_de_Archivos/productos.txt", "a") as archivo:
    archivo.write(f"\n{nombre_nuevo},{precio_nuevo},{cantidad_nueva}")

print("\nProducto agregado correctamente al archivo.")