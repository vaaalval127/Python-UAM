'''Ejercicio #1: Cola de impresión compartida
Simule el funcionamiento de una cola de impresión en una oficina donde varios empleados
envían documentos para ser impresos. Cada documento tiene un nombre, el usuario que lo
envió y el número de páginas. El sistema debe permitir agregar documentos a la cola,
procesarlos en orden de llegada y mostrar cuál es el documento que se está imprimiendo
actualmente. Analice con los estudiantes cómo se evita el desorden en el uso compartido de un
recurso limitado.'''

import os

def clear():
    os.system('cls')

class ImpresionDatos:
    def __init__(self, usuario, nombre_documento, paginas):
        self.usuario = usuario
        self.nombre_documento = nombre_documento 
        self.paginas = paginas 

    def __str__(self):
        return (f"usuario: {self.usuario}, {self.nombre_documento}, {self.paginas}")
    
class Impresora:
    def __init__(self):
        self.lista : list[ImpresionDatos] = [] # Lista con un objeto dentro que momentáneamente va a estar vacía
    
    def agregar(self, primero:ImpresionDatos): # Se guarda la clase objeto en una variable para faciliar

        self.lista.append(primero)
        print("\nDocumento agregado con éxtio!")
        
    def impresion(self):
        if self.lista:
            return self.lista.pop(0)
        else:
            return None

    def imprimirPantalla(self):
        clear()
        if self.lista:
            print("\nLista de documentos")
            for i, documento in enumerate(self.lista, start= 1):
                print(f"{i}. {documento}")
        else:
            print("No hay documentos por imprimir.")
    
def Menu():
    imprimir = Impresora()

    while True:
        print("\nMenú de opciones")
        print("1. Agregar documento")
        print("2. Imprimir documento")
        print("3. Mostrar documentos a imprimir")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            clear()
            usuario = input("\nIngrese el nombre del usuario: ")
            nombre_documento = input("Ingrese el nombre del documento que desea imprimir: ")
            paginas = int(input("Ingrese la cantidad de páginas del documento: "))
            llamada = ImpresionDatos(usuario, nombre_documento, paginas)
            imprimir.agregar(llamada)
       
        elif opcion == 2:
            impreso = imprimir.impresion()
            if impreso:
                print(f"El documento de {impreso.usuario} se está imprimiendo!")
            else:
                print("No hay documentos por imprimir.")
            
            input("Presione Enter para volver al menú de inicio")
            clear()
        
        elif opcion == 3:
            lista_docu = imprimir.imprimirPantalla()
            print(f"{lista_docu}")
        
        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Inténtelo de nuevo")

if __name__ == "__main__":
    Menu()



