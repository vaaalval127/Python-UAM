'''Desarrollar un programa que cargue los datos de un triángulo. Implementar un método/función para determinar el 
tipo d triángulo (equilátero, isósceles o escaleno)'''

print("\nPrograma que determina el tipo de triángulo.\n")

def triangulo(lado1, lado2, lado3):
        if lado1 == lado2 == lado3:
            print("El triángulo es equilátero")
        elif lado1 != lado2 != lado3:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")

def main():
    print("Ingrese el primer lado: ")
    lado1 = int(input())
    print("Ingrese el segundo lado: ")
    lado2 = int(input())
    print("Ingrese el tercer lado: ")
    lado3 = int(input())
    triangulo(lado1, lado2, lado3)

if __name__ == "__main__":
    main()
