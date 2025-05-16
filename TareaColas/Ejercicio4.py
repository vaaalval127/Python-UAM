'''Ejercicio #4: Simulación de atención de procesos por el microprocesador
Diseñe un programa que simule cómo un microprocesador atiende procesos en una cola de
ejecución. Cada proceso tiene un identificador, un nombre y una duración estimada en
milisegundos. A medida que el procesador queda libre, atiende al siguiente proceso en orden
de llegada (FIFO - First In, First Out). El sistema debe permitir agregar procesos a la cola,
mostrar el proceso en ejecución y visualizar los procesos pendientes.'''

import os

def clear():
    os.system('cls')

class Computadora:
    def __init__(self, id, nombre, milisegundos):
        self.lista = []
        self.id = id
        self.nombre = nombre
        self.milisegundos = milisegundos
    
    def __str__(self):
        return (f"Proceso ID: {self.id}, nombre: {self.nombre}, duración: {self.milisegundos}")
    
class Microprocesador:
    def __init__(self):
        self.lista : list[Computadora] = []
    
    def agregar(self, primera:Computadora): # La clase se almacena en la variable
        if len (self.lista) < 3:
            self.lista.append(primera)
            print("Proceso agregado con éxito!")
        else:
            print("Error. El procesador está saturado.")

    def atenderProcesos(self):
        if self.lista:
            return self.lista.pop(0)
        else:
            return None
    
    def imprimirPantalla(self):
        if self.lista:
            print("Lista de procesos en espera: ")
            for i, proceso in enumerate(self.lista, start=1):
                print(f"{i}. {proceso}")
        else:
            print("No hay procesos en espera.")

def Menu():
    microprocesador = Microprocesador()

    while True:
        print("\n----- Menú de opciones -----")
        print("1. Agregar proceso")
        print("2. Atender proceso")
        print("3. Mostrar procesos faltantes")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))
        clear()

        if opcion == 1:
            id = int(input("Ingrese el ID del proceso que va a realizar: "))
            nombre = input("Ingrese el nombre del proceso: ")
            milisegundos = int(input("Ingrese la duración en milisegundos del proceso: "))

            cabeza = Computadora(id, nombre, milisegundos)
            microprocesador.agregar(cabeza)
        
        elif opcion == 2:
            atendido = microprocesador.atenderProcesos()
            if atendido:
                print(f"El proceso '{atendido.nombre}' con ID: {atendido.id} ha sido atendido en {atendido.milisegundos} milisegundos!")
            else:
                print("No hay procesos por atender.")
        
        elif opcion == 3:
            lista_procesos = microprocesador.imprimirPantalla()
            print(f"{lista_procesos}")
        
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Inténtelo de nuevo.")
            input("Presione Enter para volver al inicio")
        
if __name__ == "__main__":
    Menu()