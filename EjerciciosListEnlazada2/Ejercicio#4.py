'''Se desea implementar el historial de acciones realizadas por un usuario en un editor de texto 
(como escribir, borrar, pegar, copiar). Cada acción debe guardarse en orden y poder recorrerlas 
en ambas direcciones, simulando las acciones de Deshacer y Rehacer '''

import os
import time

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

class Node:
    def __init__(self, action, texto):
        self.action = action
        self.texto = texto 
        self.prev = None
        self.next = None

class ActionHistory:
    def __init__(self):
        self.current = None
        self.head = None
        self.tail = None

    def add_action(self, action, texto):
        nuevo_nodo = Node(action, texto)
        if self.head is None:  
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo
        
        self.current = nuevo_nodo 

    def deshacer(self):
        if self.current is None:
            print("No hay acciones para deshacer.")
            return None
        accion = self.current.action
        self.current = self.current.prev 
        return accion

    def rehacer(self):
        if self.current is None or self.current.next is None:
            print("No hay acciones para rehacer.")
            return None
        self.current = self.current.next 
        return self.current.action
    def mostrar_historial(self):
        acciones = []
        nodo = self.head
        while nodo:
            acciones.append(nodo.action)
            nodo = nodo.next
        return acciones

def main():
    historial = ActionHistory()
    texto_actual = ""
    portapapeles = ""

    while True:
        limpiar()
        time.sleep(0.5)
        print("===================================")
        print("\nTexto actual:", texto_actual)
        print("Portapapeles:", portapapeles)
        print("\n===================================")
        print("\nOpciones:")
        print("1. Escribir texto")
        print("2. Borrar texto")
        print("3. Copiar texto")
        print("4. Pegar texto")
        print("5. Deshacer acción")
        print("6. Rehacer acción")
        print("7. Mostrar historial")
        print("8. Salir")
        
        opc = input("Seleccione una opción (1-8): ")

        if opc == '1':
            texto = input("Ingrese el texto a escribir: ")
            nuevo_texto = texto_actual + texto
            historial.add_action(f"Escribir: '{texto}'", nuevo_texto)
            texto_actual = nuevo_texto
            print(f"Texto escrito: '{texto}'")

        elif opc == '2':
            texto = input("Ingrese el texto a borrar: ")
            if texto in texto_actual:
                nuevo_texto = texto_actual.replace(texto, "", 1) 
                historial.add_action(f"Borrar: '{texto}'", nuevo_texto)
                texto_actual = nuevo_texto
                print(f"Texto borrado: '{texto}'")
            else:
                print(f"No se encontró el texto '{texto}' en el texto actual.")

        elif opc == '3':
            texto = input("Ingrese el texto a copiar: ")
            if texto in texto_actual:
                portapapeles = texto
                historial.add_action(f"Copiar: '{texto}'", texto_actual)
                print(f"Texto copiado: '{texto}'")
            else:
                print(f"No se encontró el texto '{texto}' en el texto actual.")

        elif opc == '4':
            if portapapeles:
                nuevo_texto = texto_actual + portapapeles
                historial.add_action(f"Pegar: '{portapapeles}'", nuevo_texto)
                texto_actual = nuevo_texto
                print(f"Texto pegado: '{portapapeles}'")
            else:
                print("El portapapeles está vacío.")

        elif opc == '5':
            accion = historial.deshacer()
            if accion:
                if historial.current: 
                    texto_actual = historial.current.texto  
                print(f"Acción deshecha: {accion}")

        elif opc == '6':
            accion = historial.rehacer()
            if accion:
                if historial.current:  
                    texto_actual = historial.current.texto 
                print(f"Acción rehecha: {accion}")

        elif opc == '7':
            while True:
                limpiar()
                print("===================================")
                print("Historial de acciones:")
                for i, accion in enumerate(historial.mostrar_historial()):
                    print(f"{i + 1}. {accion}")
                print("\n===================================")
                continuar = input("¿Desea salir del Historial? (s/n): ").lower()
                if continuar != 'n':
                    break

        elif opc == '8':
            limpiar()
            print("===================================")
            print("Saliendo del editor de texto.")
            print("===================================")
            time.sleep(1)
            break

        else:
            limpiar()
            print("===================================")
            print("\nOpción no válida. Intente de nuevo.\n")
            print("===================================")
            time.sleep(1)

if __name__ == "__main__":
    main()