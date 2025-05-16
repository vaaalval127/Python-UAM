'''Pedir la nota final de una asignatura para n estudiantes y determinar si la calificación es menor de 60 ("Reprobado"),
entre 60 y 69 ("Regular"), entre 70 y 79 ("Bueno"), entre 80 y 89 ("Muy bueno") o mayor de 89 pero menor o igual a 100 ("Excelente")'''

nota_final = list()
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

for i in range (cantidad_estudiantes):
    nota = input(f"Ingrese su nota {i+1}: ")
    if float(nota) < 60:
        print("Reprobado")
    elif float(nota) >= 60 and float(nota) <= 69:
        print("Regular")
    elif float(nota) >= 70 and float(nota) <= 79:
        print("Bueno")
    elif float(nota) >= 80 and float(nota) <= 89:
        print("Muy Bueno")
    elif float(nota) >= 90 and float(nota) <= 100:
        print("Excelente")
    else:
        print("Número inválido")
    nota_final.append(int(nota))

print(nota_final)
