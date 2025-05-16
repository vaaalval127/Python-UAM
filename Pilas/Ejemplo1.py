class Pila:
    def __init__(self):
        self.lista = []
    
    def estaVacia(self):
        return self.lista == []
    
    def agregar(self, elemento):
        self.lista.append(elemento)
    
    def extraer(self):
        return self.lista.pop()
    
    def imprimir(self):
        return self.lista
    
    def tamaño(self):
        return len(self.lista)
    
p = Pila()
print("Estado de la Pila")
print(p.estaVacia())

elemento = int(input("Agregar un elemento de tipo entero: "))
p.agregar(elemento)
elemento = float(input("Agregar un elemento de tipo decimal: "))
p.agregar(elemento)
elemento = input("Agregar un elemento: ")
p.agregar(elemento)

print("Estado de la Pila: ")
print(p.estaVacia())

print("Lista de elementos:")
print(p.imprimir())

print("Tamaño de la lista: ")
print(p.tamaño())

print("Extraer elemento: ")
print(p.extraer())

print("Estado de la Pila: ")
print(p.estaVacia())

print("Lista de elementos:")
print(p.imprimir())

print("Tamaño de la lista: ")
print(p.tamaño())
