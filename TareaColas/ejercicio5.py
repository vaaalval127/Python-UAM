'''Ejercicio #5: Gestión de acceso a archivos en un servidor
Imagina un servidor de archivos en una red donde varios usuarios solicitan acceso a un mismo
archivo compartido para su lectura. Para evitar conflictos o bloqueos, las solicitudes se atienden
en el orden en que llegan. Diseña un programa en Python que simule este comportamiento
utilizando una cola. El programa debe permitir registrar solicitudes de acceso (nombre del
usuario y archivo solicitado), mostrar qué usuario está accediendo al archivo y eliminar la
solicitud una vez atendida. También debe permitir consultar la lista de solicitudes pendientes.'''

import os

def clear():
    os.system('cls')

class Usuarios:
    def __init__(self, usuario, archivo):
        self.lista = []
        self.usuario = usuario
        self.archivo = archivo
    
    def __str__(self):
        return (f"Solicitud: {self.usuario}, archivo: {self.archivo}")
    
class GestionServidor:
    def __init__(self):
        self.lista : list[Usuarios] = []

    def agregar(self, primera:Usuarios):
        if len(self.lista) < 5:
            self.lista.append(primera)
            print("Su solicitud se ha registrado con éxito!")
        else:
            print("Error. El servidor está saturado.")
    
    def atender(self):
        if self.lista:
            return self.lista.pop(0)
        else:
            return None
    
    def ImprimirPantalla(self):
        if self.lista:
            print("Lista de archivos pendientes:")
            for i, pendiente in enumerate(self.lista, start=1):
                print(f"{i}. {pendiente}")
        else:
            print("No hay solicitudes por atender.")

def Menu():
    servidor = GestionServidor()

    while True:
        print("\n---- Menú de opciones ---- ")
        print("1. Registrar archivos")
        print("2. Atender solicitudes")
        print("3. Mostrar solicitudes en espera")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))
        clear()

        if opcion == 1:
            usuario = input("Ingrese su nombre: ")
            archivo = input("Ingrese el nombre del archivo que necesita: ")
            cabeza = Usuarios(usuario, archivo)
            servidor.agregar(cabeza)
        
        elif opcion == 2:
            atendido = servidor.atender()
            if atendido:
                print(f"La solicitud de {atendido.usuario} que solicitó el archivo '{atendido.archivo}' ha sido atendida!")
            else:
                print("No hay solicitudes por atender.")
        
        elif opcion == 3:
            lista_solicitudes = servidor.ImprimirPantalla()
            print(f"{lista_solicitudes}")
        
        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Inténtelo de nuevo.")
            input("Presione Enter para volver al inicio")
            clear()

if __name__ == "__main__":
    Menu()

