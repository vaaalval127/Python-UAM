'''Calcular la nota de n estudiantes para los tres cortes de 
evaluación de asignatura algoritmos y estructura de datos'''

print("\n")
print("Programa para calcular el promedio de los alumnos de programación \n")
n = int(input("Ingrese la cantidad de alumnos que desea promediar: "))

for contador in range(n):
    print("Ingrese el nombre del alumno: ")
    nombre = input()
    print("Ingrese la primera nota del estudiante: ")
    nota1 = float(input())
    print("Ingrese la segunda nota del estudiante: ")
    nota2 = float(input())
    print("Ingrese la tercera nota del estudianre: ")
    nota3 = float(input())
    
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio final del alumno es de: {promedio}")

    if promedio < 69 :
        print("\nReprobado")
    elif promedio >= 70 and promedio <= 79:
        print("\nRegular")
    elif promedio >= 80 and promedio <= 89:
        print("\nBueno")
    elif promedio >= 90 and promedio <= 100:
        print("\nExcelente")

print("\n")
