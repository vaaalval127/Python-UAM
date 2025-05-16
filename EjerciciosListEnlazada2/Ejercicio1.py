'''Problema#1
Una escuela de educación primaria requiere un algoritmo que muestre los datos de los
estudiantes de un salón de clase ordenados de forma ascendente, según un parámetro
indicado; este parámetro puede ser cualquiera de los siguientes campos: carnet, nombres,
apellidos, peso, estatura, sexo, promedio.'''

class Estudiante:
    def __init__(self, carnet, nombres, apellidos, peso, estatura, sexo, promedio):
        self.carnet = carnet
        self.nombres = nombres
        self.apellidos = apellidos
        self.peso = peso
        self.estatura = estatura
        self.sexo = sexo
        self.promedio = promedio

    def __str__(self): # Método para representar el estudiante como una cadena de texto
        return (f"Carnet: {self.carnet}, Nombres: {self.nombres}, Apellidos: {self.apellidos}, "f"Peso: {self.peso}, Estatura: {self.estatura}, Sexo: {self.sexo}, Promedio: {self.promedio}")

class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, estudiante):
        nuevo_nodo = Nodo(estudiante) # Si la lista está vacía, el nuevo nodo se convierte en la cabeza de la lista
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza # Comienza desde la cabeza de la lista
            while actual.siguiente: # Recorre la lista hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def ordenar(self, atributo):
        if not self.cabeza or not self.cabeza.siguiente: # Si la lista está vacía o 
            #tiene un solo nodo, no hay nada que ordenar
            return  # No hay nada que ordenar

        # Convertir la lista enlazada a una lista normal para facilitar el ordenamiento
        lista = [] #lista vacía para almacenar los estudiantes
        actual = self.cabeza # Comienza desde la cabeza 
        while actual: # Recorre la lista enlazada
            lista.append(actual.estudiante) # Agrega el estudiante a la lista
            actual = actual.siguiente

        # Ordenar la lista usando el atributo
        lista.sort(key=lambda estudiante: getattr(estudiante, atributo))

        # Reconstruir la lista enlazada ordenada
        self.cabeza = None # Reinicia la cabeza de la lista
        for estudiante in lista: # Recorre la lista ordenada
            self.agregar(estudiante)    # Agrega cada estudiante a la lista enlazada

    def mostrar(self):
        actual = self.cabeza # Comienza desde la cabeza de la lista
        while actual:
            print(actual.estudiante) # Muestra el estudiante actual
            actual = actual.siguiente # Avanza al siguiente nodo

def main():
    # Crear la lista enlazada
    lista_estudiantes = ListaEnlazada()

    # Ingresar datos de los estudiantes
    print("\nIngrese los datos de los estudiantes (deje el carnet vacío para terminar):")
    while True:
        carnet = input("Carnet: ").strip()
        if carnet == "":
            break # Termina la entrada si el carnet está vacío
        nombres = input("Nombres: ").strip()
        apellidos = input("Apellidos: ").strip()
        peso = float(input("Peso (kg): ").strip())
        estatura = float(input("Estatura (m): ").strip())
        sexo = input("Sexo (M/F): ").strip().upper()
        promedio = float(input("Promedio: ").strip())
        lista_estudiantes.agregar(Estudiante(carnet, nombres, apellidos, peso, estatura, sexo, promedio))

    # Mostrar estudiantes antes de ordenar
    print("\nEstudiantes antes de ordenar:")
    lista_estudiantes.mostrar()

    # Solicitar el atributo para ordenar
    print("\nAtributos disponibles para ordenar: carnet, nombres, apellidos, peso, estatura, sexo, promedio")
    atributo = input("Ingrese el atributo por el cual desea ordenar: ").strip()

    # Ordenar por el atributo ingresado
    lista_estudiantes.ordenar(atributo)

    # Mostrar estudiantes después de ordenar
    print(f"\nEstudiantes después de ordenar por {atributo}:")
    lista_estudiantes.mostrar()

if __name__ == "__main__":
    main()