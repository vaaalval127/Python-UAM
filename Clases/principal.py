from clase_empleado import Empleado

def main():
    empleados = []
    print("Ingrese la cantidad de empleados: ", end='')
    n = int(input())

    print("Ingrese los datos de los empleados: ", end='')
    for i in range(n):
        print("Nombre ",  end='')
        nombre = input()
        print("Salario bruto: ", end='')
        salBruto = float(input())

        emp = Empleado(nombre, salBruto)

        empleados.append(emp)

    print("Datos de Empleados")
    for emp in empleados:
        x = emp.get_salarioNeto()
        print(f"{emp.get_nombre()}: {x}")

if __name__ == "__main__":
    main()

