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
"""

with open("Unidad_8_Manejo_de_Archivos/productos.txt", "w") as archivo:
    archivo.write("Shampoo,1500,20\n")
    archivo.write("Acondicionador,1800,15\n")
    archivo.write("Gel,1200,10\n")

print(f"Archivo creado")


2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
formato: 


with open("Unidad_8_Manejo_de_Archivos/productos.txt", "r") as archivo:
    print("Listado de productos:\n")
    
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
            
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
cantidad) y lo agregue al archivo sin borrar el contenido existente.



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

"""


"""
4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
una lista llamada productos, donde cada elemento sea un diccionario con claves: 
nombre, precio, cantidad.
"""

productos = []

with open("Unidad_8_Manejo_de_Archivos/productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue  # salta líneas vacías
        partes = linea.split(",")
        if len(partes) != 3:
            print(f"Línea inválida encontrada y omitida: {linea}")
            continue
        nombre, precio, cantidad = partes

        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print("Listado de productos cargados en memoria:\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

"""
5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
no existe, mostrar un mensaje de error. 
"""

print("\n--- Buscar producto por nombre ---")
buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()

encontrado = False
for p in productos:
    if p["nombre"].lower() == buscado:
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nProducto no encontrado en la lista.")
    
"""
6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
productos actualizados desde la lista. 
"""

with open("Unidad_8_Manejo_de_Archivos/productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)
        
print("\nArchivo productos.txt actualizado correctamente.")
