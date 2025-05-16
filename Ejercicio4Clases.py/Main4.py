'''Ejercicio #4: Gestión de productos e inventario
Diseñar una clase Producto que incluya atributos como código, nombre, precio y
cantidad en stock. Además, los estudiantes deberán implementar una clase
Inventario que administre una colección de objetos Producto, incorporando
métodos para agregar, buscar, actualizar y eliminar productos. Este ejercicio
permite modelar situaciones reales de gestión de ventas y refuerza el concepto
de encapsulación y manejo de colecciones en programación orientada a objetos.'''

import os
def limpiar_pantalla():
    os.system('cls')

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad_stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    def __str__(self):
        return f"Producto({self.codigo}): {self.nombre}, Precio C${self.precio:.2f}, Cantidad en Stock: {self.cantidad_stock}"

    def actualizarProducto(self, nombre = None, precio = None, cantidad = None):
        if nombre:
            self.nombre = nombre
        elif precio is not None:
            self.precio = precio
        if cantidad is not None:
            self.cantidad_stock = cantidad
            
class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"El producto con código {producto.codigo} ya existe.")
        else:
            self.productos[producto.codigo] = producto
            print(f"Producto {producto.nombre} agregado correctamente.")

    def buscar_producto(self, codigo):
        return self.productos.get(codigo)

    def actualizar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto:
            print("Ingresa los nuevos datos (deja en blanco si no deseas cambiar un campo):")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = input("Nuevo precio: ")
            nueva_cantidad = input("Nueva cantidad: ")

            producto.actualizarProducto(
                nombre = nuevo_nombre if nuevo_nombre else None,
                precio = float(nuevo_precio) if nuevo_precio else None,
                cantidad = int(nueva_cantidad) if nueva_cantidad else None
            )
            print("Producto actualizado.")
        else:
            print(f"Producto con código {codigo} no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            print(f"Producto {codigo} eliminado.")
        else:
            print(f"Producto con código {codigo} no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(f"  - {producto}")

def Menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = int(input("\nIngrese la acción que desea realizar: "))
        limpiar_pantalla()
        match opcion:
            case 1:
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                producto = Producto(codigo, nombre, precio, cantidad)
                inventario.agregar_producto(producto)
            case 2:
                codigo = input("Código del producto a buscar: ")
                producto = inventario.buscar_producto(codigo)
                
                if producto:
                    print("Producto encontrado:", producto)
                else:
                    print("Producto no encontrado.")
            case 3:
                codigo = input("Código del producto a actualizar: ")
                inventario.actualizar_producto(codigo)
            case 4:
                codigo = input("Código del producto a eliminar: ")
                inventario.eliminar_producto(codigo)
            case 5:
                inventario.mostrar_inventario()
            case 6:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")
Menu()