'''Un estudiante universitario desea llevar el control de sus gastos mensuales
relacionados con sus estudios, como transporte, alimentación, materiales educativos,
conexión a internet, alquiler, entre otros.
Desarrolla una aplicación en Python que le permita al estudiante:
1. Registrar sus categorías de gastos.
2. Agregar múltiples gastos individuales, indicando:
− Fecha (como cadena de texto)
− Categoría (de las previamente registradas)
− Monto del gasto
− Descripción corta
3. Mostrar el total gastado en el mes.
4. Mostrar el total por cada categoría.
5. Listar todos los gastos realizados.
6. Mostrar el gasto promedio por categoría.'''

from controlGastos import ControlGastos
import categorias
import gastos
import reportes

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar categoría")
    print("2. Mostrar categorías")
    print("3. Agregar gasto")
    print("4. Listar gastos")
    print("5. Total gastado")
    print("6. Total por categoría")
    print("7. Promedio por categoría")
    print("8. Salir")

control = ControlGastos()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        categorias.agregarCategoria(control)
    elif opcion == "2":
        categorias.mostrarCategorias(control)
    elif opcion == "3":
        gastos.agregarGasto(control)
    elif opcion == "4":
        gastos.listar_gastos(control)
    elif opcion == "5":
        reportes.mostrar_total(control)
    elif opcion == "6":
        reportes.mostrar_total_por_categoria(control)
    elif opcion == "7":
        reportes.mostrar_promedio_por_categoria(control)
    elif opcion == "8":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida.")
    