'''Ejercicio #2: Gestión de llamadas en un centro de atención al cliente
Cree un sistema que simule la atención de llamadas en un Call Center. Cada llamada debe
ingresar a una cola con datos como el nombre del cliente y el motivo de la llamada. A medida
que los agentes estén disponibles, se debe atender al siguiente cliente en orden de llegada.'''

import os

def clear():
    os.system('cls')

class GestionLLamada:
    def __init__(self, usuario, motivo):
        self.lista = []
        self.usuario = usuario
        self.motivo = motivo
    
    def __str__(self):
        return (f"Usuario: {self.usuario}, {self.motivo}")
    
class Llamadas:
    def __init__(self):
        self.lista : list[GestionLLamada] = []

    def agregar(self, primero:GestionLLamada): # Se guarda la clase en una variable para faciliar la herencia
        self.lista.append(primero)
        print("Llamada en espera!")

    def atender(self):
        if self.lista:
            return self.lista.pop(0)
        else:
            return None
    
    def imprimirLista(self):
        clear()
        if self.lista:
            for i, llamada in enumerate(self.lista, start=1):
                print(f"{i}. {llamada}")
        else:
            print("No hay llamadas en espera.")

def Menu():
    llamada = Llamadas()

    while True:
        print("\nMenú de opciones")
        print("1. Registrar llamada")
        print("2. Atender llamada")
        print("3. Mostrar llamadas por atender")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            clear()
            usuario = input("Ingrese su nombre: ")
            motivo = input("Ingrese el motivo de la llamada: ")
            primera = GestionLLamada(usuario, motivo)
            llamada.agregar(primera)
        
        elif opcion == 2:
            atendido = llamada.atender()
            if atendido:
                print(f"La llamada del usuario {atendido.usuario} ha sido atendida!")
            else:
                print("No hay llamadas en espera.")
        
        elif opcion == 3:
            lista_llamada = llamada.imprimirLista()
            print(f"{lista_llamada}")
        
        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Ingrese una opción válida.")

if __name__ == "__main__":
    Menu()