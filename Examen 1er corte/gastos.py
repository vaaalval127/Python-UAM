def agregarGasto(control):
    fecha = input("Fecha del gasto: ")
    categoria = input("Categoría del gasto: ")
    try:
        monto = float(input("Monto: "))
        descripcion = input("Descripción ")
        control.agregarGasto(fecha, categoria, monto, descripcion)
    except ValueError:
        print("Monto inválido.")

def listar_gastos(control):
    control.listarGastos()
    