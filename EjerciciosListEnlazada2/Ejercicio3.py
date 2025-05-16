'''Problema#3
Una clínica recibe pacientes en orden de llegada. Cada paciente debe ser ingresado al sistema
con los siguientes datos: nombre completo, edad, síntoma principal y prioridad (de 1 a 5). El
sistema debe permitir insertar nuevos pacientes, recorrer la lista para mostrar el orden de
atención, y eliminar a un paciente una vez atendido.'''

import os
def limpiar_pantalla():
    os.system("cls")

class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

class ListaPacientes:
    def __init__(self):
        self.inicio = None
    
    def agregarPaciente(self,paciente):
        nuevo = Nodo(paciente)
        if self.inicio is None:
            self.inicio = nuevo
            return
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def imprimir(self):
        if self.inicio is None:
            print("No hay pacientes en la lista.")
        else:
            actual = self.inicio
            while actual: # Mientras hayan nodos por recorrer
                paciente = actual.paciente # Actual es cada nodo y con .paciente se accede a los datos del paciente
                print(f"Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Síntoma: {paciente['sintoma']}, Prioridad: {paciente['prioridad']}")
                actual = actual.siguiente
    
    def atender(self):
        if self.inicio is not None:
            atendido = self.inicio.paciente
            self.inicio = self.inicio.siguiente
            return atendido
        else:
            return None
        
def Menu():
    lista = ListaPacientes()
    
    while True:
        print("\nMenú de opciones\n")
        print("1. Ingresar pacientes")
        print("2. Mostrar pacientes")
        print("3. Atender pacientes")
        print("4. Salir")

        opcion = int(input("Ingrese la opción que desea desarrollar: "))
        limpiar_pantalla()

        if opcion == 1:
            print("Ingrese los datos del paciente")
            nombre = input("Nombre completo: ")
            edad = int(input("Edad: "))
            sintoma = input("¿Qué síntomas presenta?: ")
            prioridad = int(input("Prioridad (1 a 5): "))

            paciente = {
                    "nombre": nombre,
                    "edad": edad,
                    "sintoma": sintoma,
                    "prioridad": prioridad
                }
            limpiar_pantalla()
            lista.agregarPaciente(paciente)
            print("\nPaciente agregado exitosamente!")

        elif opcion == 2:
            print("Lista de pacientes: ")
            lista.imprimir()

        elif opcion == 3:
            atendido = lista.atender()
            if atendido:
                print(f"Paciente atendido: {atendido['nombre']}")
            else:
                print("No hay pacientes por atender.")

        elif opcion == 4:
            break
        
        else:
            print("Opción Inválida. Vuelva a intentarlo nuevamente")

if __name__ == "__main__":
    Menu()