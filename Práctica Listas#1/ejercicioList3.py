'''Desarrollar un programa que se comporte como un diccionario Inglés-Español; esto es, solicitará
una palabra en inglés y escribirá la correspondiente palabra en español. Para hacer más sencillo
el ejercicio, el número de parejas de palabras estará limitado a 5. Por ejemplo, suponer que
introducimos las siguientes parejas de palabras:

book libro
green verde
mouse ratón

Una vez finalizada la introducción de las listas de palabras, pasamos al modo traducción, de
forma que si introducimos green, la respuesta ha de ser verde. Si la palabra no se encuentra, se
emitirá un mensaje que lo indique.

El programa constará de dos métodos, aparte de Main():
1. crearDiccionario(). Este método creará el diccionario.
2. traducir(). Este método realizará la labor de traducción.'''

import os
def limpiar_pantalla():
    os.system('cls')

print("\nDiccionario Inglés-Español")

diccionario = {}

def crearDiccionario():
    print("\n   Introduzca 5 pares de palabras en inglés y español: \n")

    for i in range(2):
        print("Palabras en inglés: ", end='')
        palabras_ingles = input()

        print("Palabras en español: ", end='')
        palabras_español = input()

        diccionario[palabras_ingles] = palabras_español
    return diccionario

def traducir(dicionario):
    limpiar_pantalla()

    print("Ingrese la palabra que desee traducir: ")
    palabra = input()
    
    limpiar_pantalla()

    if palabra in diccionario:
        print(f"La traducción de {palabra} es {diccionario[palabra]}")
    else:
        print("Palabra no encontrada.")

def Main():
    diccionario = crearDiccionario()
    traducir(diccionario)

if __name__ == "__main__":
    Main()