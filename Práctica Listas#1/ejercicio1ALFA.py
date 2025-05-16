'''Crear un programa que simule la gestión de un inventario en una tienda. Utilizar un menú para agregar, eliminar, 
modificar y consultar productos en el inventario. Cada producto tendrá un código, nombre, cantidad y precio.


Menú de opciones:
1. Agregar producto
2. Eliminar producto
3. Modificar producto
4. Consultar producto
5. Mostrar todos los productos
6. Salir'''

import os
def limpiar_pantalla():
    os.system('cls')
    
print("\n")
print("Programa para gestión de inventario en una tienda \n")

lista_productos  = [[1111, 'pan', 30, 60]]

while True :
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Modificar producto")
    print("4. Consultar producto")
    print("5. Mostrar producto")
    print("6. Salir")

    opcion = int(input("Ingrese la opción que desea desarrollar: "))
    limpiar_pantalla()
    match opcion:
        case 1:
            print("Ingrese el codigo del producto que desea agregar: ")
            codigo = int(input())
            print("Ingrese el nombre del producto: ")
            nombre_producto = input()
            print("Ingrese la cantidad que desea agregar: ")
            cantidad_producto = int(input())
            print("Ingrese el precio del producto: ")
            precio_producto = float(input())

            producto = [codigo, nombre_producto, cantidad_producto, precio_producto]
            lista_productos.append(producto)

            print("\nEl producto ha sido agregado con éxito! \n")
        case 2:
            print("Ingrese el código del producto que desea eliminar: \n")
            
            codigo_producto_eliminar = int(input())
            lista_productos = [producto for producto in lista_productos if isinstance(producto, list) and len(producto) > 0 and producto[0] != codigo_producto_eliminar]
            # Para todos los productos en la lista de productos, si el codigo está en la lista (insinstance) y la lista no está vacía, 
            # se elimina el producto que tenga el mismo valor que lo que el usuario introdujo
            print("El producto se ha eliminado exitosamente! ")
        case 3:
            print("¿Qué producto desea modificar? ")
            codigo_producto_modificar = int(input())

            for producto in lista_productos:
                if producto [0] == codigo_producto_modificar:
                    print(f"Producto encontrado: {producto}")

                    producto[1] = input("Ingrese el nuevo nombre del producto: \n")
                    producto[2] = int(input("Ingrese la nueva cantidad que desea agregar: \n"))
                    producto[3] = float(input("Ingrese el nuevo precio del producto: \n"))
                    
                    print("Producto modificado exitosamente!")
                    break
                else:
                    print("Producto no encontrado.")
        case 4:
            print("Indique el producto que desea consultar: ", end='')
            producto_consultar = int(input())

            for producto in lista_productos:
                if producto [0] == producto_consultar:
                    print("-" * 100)
                    print(f"Producto encontrado: Código: {producto[0]} |  Nombre: {producto[1]} |  Cantidad: {producto[2]} |  Precio: {producto[3]}")
                    print("-" * 100)
                    break
                else:
                    print("Producto no encontrado.")
        case 5:
            print("\n Lista de productos en inventario:")
            print("-" * 100)
            for producto in lista_productos:
                print(f" Código: {producto[0]} |  Nombre: {producto[1]} |  Cantidad: {producto[2]} |  Precio: {producto[3]}")
            print("-" * 100)
                
        case 6:
            print("Saliendo del programa... Adiós")
            break
        case _:
            print("Opción invpalida.")