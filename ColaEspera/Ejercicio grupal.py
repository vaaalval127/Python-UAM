'''Programa de pedidos en línea'''

import os
import time

def clear():
    os.system('cls')
    time.sleep(0.5)

class Pedido:
    def __init__(self):
        self.pedidos = []

    def agregar(self, nombre_cliente, direccion, producto, cantidad):
        self.pedidos.append({"nombre_cliente": nombre_cliente, "direccion": direccion, "producto": producto, "cantidad": cantidad})
        print(f"Pedido agregado: {cantidad} de {producto} para {nombre_cliente}.")

    def entregar(self):
        if self.pedidos:
            entregado = self.pedidos.pop(0)
            print(f"El pedido de {entregado['cantidad']} de {entregado['producto']} para {entregado['nombre_cliente']} ha sido entregado.")
            time.sleep(1.5)
        else:
            print("No hay pedidos en la lista.")

    def imprimir(self):
        if self.pedidos:
            print("Lista de pedidos:\n")
            for i, pedido in enumerate(self.pedidos, start=1):
                print(f"{i}. {pedido['cantidad']} de {pedido['producto']} para {pedido['nombre_cliente']} en: ({pedido['direccion']}).")
        else:
            print("No hay pedidos en la lista.")

def menu():
    pedido = Pedido()
    while True:
        clear()
        print("=======================\n")
        print(f"Pedidos pendientes: {len(pedido.pedidos)}")
        print("Pedido a entregar: ", end="")
        if pedido.pedidos:
            print(f"{pedido.pedidos[0]['cantidad']} de {pedido.pedidos[0]['producto']} para {pedido.pedidos[0]['nombre_cliente']}")
        else:
            print("No hay pedidos pendientes.")
        print("\n=======================")
        print("\n--- Menú de Pedidos ---")
        print("1. Agregar pedido")
        print("2. Lista de pedidos")
        print("3. Entregar pedido")
        print("4. Salir")

        opc = input("Seleccione una opción: ")

        if opc == "1":
            clear()
            print("====================================================")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección de entrega: ")
            producto = input("Ingrese el producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            pedido.agregar(nombre_cliente, direccion, producto, cantidad) 
        elif opc == "2":
            clear()
            pedido.imprimir()
            input("Presione Enter para volver al menú principal...\n")
        elif opc == "3":
            clear()
            pedido.entregar()
        elif opc == "4":
            clear()
            print("=======================")
            print("\nSaliendo del programa.\n")
            print("=======================")
            clear()
            break
        else:
            print("\nOpción inválida. Intentelo nuevamente.")
            time.sleep(1)

if __name__ == "__main__":
    menu()