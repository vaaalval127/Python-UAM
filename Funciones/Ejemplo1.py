'''Ejercicios de funciones con Python: suma, menor y mayor de los números'''
# Definición de funciones
def suma(lista):
    total = 0
    for x in lista:
        total = total + x
    return (total)

def menor(lista):
    men = lista[0]
    for x in lista:
        if x < men:
            men = x
    return(men)

def mayor(lista):
    mayo = lista[0]
    for x in lista:
        if x > mayo:
            mayo = x
    return(mayo)

# Programa principal
def main():
    lista = []
    print("Ingrese la cantidad de elementos a procesar: ", end='')
    n = int(input())

    #Captura de datos
    for i in range(n):
        print(f"Ingrese el elemento {i + 1}: ", end='')
        num = int(input())
        lista.append(num)
    
    #Llamando a las funciones
    print("Los elementos de la lista son: ", lista)
    print("La suma de todos los elementos es: ", suma(lista))
    print("El número menor de la lista es: ", menor(lista))
    print("El número mayor es: ", mayor(lista))

if __name__ == "__main__":
    main()
