'''Desarrollar un programa que permita al usuario gestionar una cuenta bancaria. El programa 
deberá utilizar un menú que permita realizar diferentes operaciones sobre el saldo de la cuenta.
Menú de opciones:

1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir

El programa debe permitir al usuario ingresar la cantidad para depositar o retirar, actualizar el
saldo y mostrar los resultados. Si se elige la opción de retiro, debe verificar que el saldo sea
suficiente.'''

print("\nPrograma que permita gestionar una cuenta bancaria \n")

numero_de_cuenta = [1111222233334444]
pin_cuenta = [1234]
cuenta_bancaria = [1000, 'pesos']

import os
def limpiar_pantalla():
    os.system('cls')

while True:
    print("Ingrese su número de cuenta bancaria: ", end='')
    numero_cuenta = int(input())
    if numero_cuenta in numero_de_cuenta:
        print("Su cuenta ha sido verificada!")
        break
    else:
        print("Cuenta no encontrada. Inténtelo de nuevo.")

while True:
    print("\nIngrese su pin de acceso al sistema:\n", end='')
    pin = int(input())
    limpiar_pantalla()
    if pin in pin_cuenta:
        print("\nAccediendo al sistema...\n")
        break
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")    

while True:
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = int(input("\n¿Qué acción desea realizar?\n "))
    limpiar_pantalla()
    match opcion:
        case 1:
            saldo = cuenta_bancaria[0]
            moneda = cuenta_bancaria[1]
            print(f"Su saldo actual es de : {saldo} {moneda}\n")
        case 2:
            print("Ingrese la cantidad (monto) que desea depositar en la cuenta: ", end='')
            monto_depositar = float(input())

            cuenta_bancaria [0] = float(cuenta_bancaria[0]) + monto_depositar
            print(f"\nEl depósito se realizó exitosamente. Su monto final es de: {cuenta_bancaria[0]} {cuenta_bancaria[1]}\n")
        case 3:
            print("Ingrese el total (monto) que desea retirar: ")
            monto_retirar = float(input())

            if monto_retirar <= cuenta_bancaria[0]:
                
                cuenta_bancaria[0] = float(cuenta_bancaria[0]) - monto_retirar
                print(f"\nRetiro exitoso. Su saldo actual es de: {cuenta_bancaria[0]} {cuenta_bancaria[1]}\n")
            else:
                print("Monto insuficiente.")
        case 4:
            print("Saliendo del programa... Adiós")
            break
        case _:
            print("Opción inválida.")