class Cola:
    def __init__(self):
        self.lista = []

    def EstaVacia(self):
        return len(self.lista) == 0 # Regresa un true si está vacía y un false si está llena (el len para saber qué hay en la lista)
    
    def encolar(self, nombre): # (agregar)
        self.lista.append(nombre) # Agrega el elemento a la lista
        if len(self.lista) >= 5:
            print("La cola está llena.")
            return None
    
    def desencolar(self): # (quitar)
        return self.lista.pop(0) # Quitar el elemento de la lista
    
    def verFrente(self): # (ver el siguiente)
        return self.lista[0] # verifica el índice
    
    def Imprimir(self):
        return self.lista
    
def menu():
    cola = Cola()
    while True:
        print("\nClientes en espera:", len(cola.lista))

        print("Menú de opciones")
        print("1. Agregar clientes")
        print("2. Atender clientes")
        print("3. Verificar si cola está vacía")
        print("4. Ver siguiente cliente a atender")
        print("5. Imprimir lista de clientes")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre del cliente: ")
            cola.encolar(nombre)

        elif opcion == 2:
            atendido = cola.desencolar()
            if atendido:
                print(f"El cliente {atendido} ha sido atendido.")
            else:
                print("La cola está vacía")

        elif opcion == 3:
            if cola.EstaVacia():
                print("La cola está vacía.")
            else:
                print("La cola NO está vacía.")

        elif opcion == 4:
            siguiente = cola.verFrente()
            if siguiente:
                print(f"El sigueinte cliente a ser atendido es {siguiente}")
            else:
                print("La lista está vacía.")

        elif opcion == 5:
            print("Lista de clientes en espera", cola.Imprimir())

        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Intente de nuevo elegir su opción.")

if __name__ == "__main__":
    menu()