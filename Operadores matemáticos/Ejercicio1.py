'''Elabore un programa que solicite do números enteros y presente 
como resultados cada una de las respuestas de todos los operadores matemáticos.'''

num1 = float(input("Ingrese la primera cifra numérica: \n"))
num2 = float(input("Ingrese la segunda cifra numérica: \n"))

# Suma
suma = num1 + num2
print("El resultado de la suma es: ", suma)
print("\n")

# Resta
rest = num1 - num2
print("El resultado de la resta es: ", rest)
print("\n")

# Multiplicación
prod = num1 * num2
print("El resultado de la multiplicación es: ", prod)
print("\n")

# División
div = num1 / num2
print("El resultado de la división es: ", div)
print("\n")

# Módulo
mod = num1 % num2
print("El módulo de la división es: ", mod)
print("\n")

# Exponencial
expo = num1 ** num2
print("El resultado es: ", expo)
print("\n")
