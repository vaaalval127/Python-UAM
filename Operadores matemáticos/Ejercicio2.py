'''Elabore un programa para calcular la quinta potencia, la raíz cuadrada, el exponencial, el logaritmo natural, y el 
valor absoluto de un número introducido por el teclado.'''

import math
print("Porgrana para calcular la quinta potencia, la raíz cuadrada, el exponencial, el logritmo natural, y el valor absoluto. \n")
num = int(input("Ingrese el número que desee calcular: "))

#Quinta potencia
pot = num ** 5
print(f"La quinta potencia es: {pot} ")

# Raiz Cuadrada
raiz_cuadrada = math.sqrt(num)
print(f"La raíz cuadrada es: {raiz_cuadrada:,.2f}")

# Exponencial
exponent = math.exp(num)
print(f"El exponencial del número es: {exponent:,.2f}")

# Logaritmo Natural
ln = math.log(num)
print(f"El logaritmo naturral (Ln) del número es: {ln:,.2f}")

# Valor Absoluto
valor_absolut = abs(num)
print(f"El valor absoluto del número es: {valor_absolut}")
