horas = float(input("Ingrese el número de horas trabajadas: "))
salario = float(input("Ingrese el salario neto por hora: \n"))

if horas > 48 :
    total = (48 * salario) + (horas - 48) * salario * 2
else :
    total = horas * salario

print(f"Su pago total es de {total}")

