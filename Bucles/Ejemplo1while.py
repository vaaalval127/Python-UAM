'''Calcular la nota de n estudiantes para los tres cortes de 
evaluación de asignatura algoritmos y estructura de datos'''

print("\n")
print("Programa para calcular el promedio final de los alumnos de programación \n")
cant_alumnos = int(input("A continuación, ingrese la cantidad de alumnos que desea promediar: "))

i = 0
while i < cant_alumnos :
    nota1 = int(input("Ingrese la primera nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercera nota: "))
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio del alumno {i + 1} es: {promedio}")
    print(i)

    if promedio < 69 :
        print("\nReprobado")
    elif promedio >= 70 and promedio <= 79:
        print("\nRegular")
    elif promedio >= 80 and promedio <= 89:
        print("\nBueno")
    elif promedio >= 90 and promedio <= 100:
        print("\nExcelente")
    i += 1 # Para que aumente la primera i del while

print("\n\n")
