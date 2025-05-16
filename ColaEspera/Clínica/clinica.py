
'''Programa de atención al cliente'''

class Clinica:
    def __init__(self):
        self.pacientes = []

    def registrar(self, paciente):
        self.pacientes.append(paciente)
    
    def atender(self):
        if self.pacientes:
            atendido = self.pacientes.pop(0)
            print(f"El paciente {atendido} ha sido atendido.")
        else:
            print("No hay pacientes en la lista de espera.")
    
    def imprimir(self):
        if self.pacientes:
            print("La lista de pacientes en espera de atención.")
            for i, paciente in enumerate(self.pacientes, start=1): # se puede sacar en tupla (para que se imprima en vertical) 
                #start es el indicador de "i" dice donde empieza a contar a partir de 1"
                print(f"{i}. {paciente}")
        else:
            print("No hay pacientes en la lista de espera.")

def menu():
    clinica = Clinica()

    while True:
        print("\nMenú de opciones")
        print("1. Agregar pacientes")
        print("2. Atender paciente ")
        print("3. Imprimir lista de espera")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre: ")
            clinica.registrar(nombre)
            print("El paciente ha sido registrado exitosamente!")
        
        elif opcion == 2:
            clinica.atender()
        
        elif opcion == 3:
            clinica.imprimir()
        
        elif opcion == 4:
            print("Saliendo del programa...")
            break

        else:
            print("Opción incorrecta. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()