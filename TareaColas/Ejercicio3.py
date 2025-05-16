'''Ejercicio #3: Gestión de turnos en una farmacia
Implemente un sistema de turnos en una farmacia, donde los pacientes son atendidos en el
orden en que llegan. Cada paciente tiene un nombre y un tipo de servicio (compra, consulta,
receta). El sistema debe permitir registrar nuevos pacientes, atender al siguiente en la fila y
mostrar los turnos pendientes.'''

import os

def clear():
    os.system('cls')

class Clientes:
    def __init__(self, nombre, servicio):
        self.lista = []
        self.nombre = nombre
        self.servicio = servicio
    
    def __str__(self):
        return (f"Cliente: {self.nombre}, servicio: {self.servicio}")
    
class GestionFarmacia:
    def __init__(self):
        self.lista : list[Clientes] = []
    
    def agregar(self, cabeza:Clientes):
        self.lista.append(cabeza)
        print("El cliente ha sido registrado con éxito!")
    
    def atender(self):
        if self.lista:
            return self.lista.pop(0)
        else:
            return None
    
    def ImprimirPantalla(self):
        if self.lista:
            for i, cliente in enumerate(self.lista, start=1):
                print(f"{i}. {cliente}")
        else:
            print("No hay clientes por atender.")

def Menu():
    farmacia = GestionFarmacia()

    while True:
        print("\n------ Menú de opciones ------")
        print("1. Agregar clientes")
        print("2. Atender cliente")
        print("3. Mostrar lista de clientes")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))
        clear()

        if opcion == 1:
            nombre = input("Ingrese su nombre: ")
            servicio = input("Ingrese el tipo de servicio que necesita: ")
            llamada = Clientes(nombre, servicio) # La clase se guarda en una variable y se hace la herencia de datos
            farmacia.agregar(llamada)
        
        elif opcion == 2:
            atendido = farmacia.atender()
            if atendido:
                print(f"El cliente {atendido.nombre} que solicitó el servicio '{atendido.servicio}' ha sido atendido!")
            else:
                print("No hay clientes por atender.")
        
        elif opcion == 3:
            lista_clientes = farmacia.ImprimirPantalla()
            print(f"{lista_clientes}")
        
        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Inténtelo de nuevo.")
            input("Presione Enter para volver al inicio")

if __name__ == "__main__":
    Menu()
