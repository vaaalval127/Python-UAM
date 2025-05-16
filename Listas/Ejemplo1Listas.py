'''Control de ventas de los empleados (3) de una empresa de electrodomésticos para un trimestre'''

tabla_empleados = []
tabla_ventas = []

for i in range(3):
    print(f"\n Ingrese el nombre del empleado {i + 1} : ", end='') # La f es para poder poner una expresión dentro de un print
    nombre = input()
    tabla_empleados.append(nombre)

for fil in range(3):
    fila = []
    for col in range(3):
        print(f"\n Ingrese la venta del empleado {fil + 1} del mes {col + 1} : ") # La f es para poder poner una expresión dentro de un print
        venta = float(input())
        fila.append(venta)
    tabla_ventas.append(fila)

print("\n Empleados: ", tabla_empleados)
print("\n Ventas: ", tabla_ventas)

print("\n Información de ventas ")
print("Nombre\tEnero\tFebrero\tMarzo")

for i, nombre in enumerate(tabla_empleados) :
    print(f"{nombre} \t{tabla_ventas[i][0]:,.1f}\t{tabla_ventas[i][1]:,.1f}\t{tabla_ventas[i][2]:,.1f}") # [] [] son las matrices y como se van moviendo