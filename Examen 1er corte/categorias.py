def agregarCategoria(control):
    nombre = input("Ingrese el nombre de la categoría: ")
    control.agregarCategoria(nombre)

def mostrarCategorias(control):
    control.mostrarCategoria()
    