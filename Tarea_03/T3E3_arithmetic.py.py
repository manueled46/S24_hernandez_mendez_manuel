"""
Date: 2021-11/22
Authors: Manuel Yahir Hernandez Mendez
File:     T3E3_arithmetic.py
Brief:   Operaciones de numeros flotantes
Score:
Version: 1
Fixes:
"""
def suma(a, b):
    res = 0.0
    res = a + b
    return res


def resta(a, b):
    res = 0.0
    res = a - b
    return res


def multiplicacion(a, b):

    res = 0.0
    res = a * b
    return res


def division(a, b):

    res = 0.0
    res = a / b
    return res


if __name__ == '__main__':
    resultado1 = 0.0
    resultado2 = 0.0
    resultado3 = 0.0
    numero1 = 1
    numero2 = 5
    numero3 = 6
    numero4 = 7
    numero5 = 9

    # para el segundo ejemplo

    resultado1 = suma(numero1, numero5)
    print("Para la suma ", resultado1)
    resultado1 = resta(numero1, numero5)
    print("Para la resta ", resultado1)
    resultado1 = multiplicacion(numero1, numero5)
    print("Para la multiplicacion ", resultado1)
    resultado1 = division(numero1, numero5)
    print("Para la division ", resultado1)

    # Para el segundo ejemplo

    print("-----------------------------")
    print("Ejemplo 2")
    print("-----------------------------")
    resultado2 = suma(numero4, numero5)

    print("Para la suma ", resultado2)
    resultado2 = resta(numero4, numero5)
    print("Para la resta ", resultado2)
    resultado2 = multiplicacion(numero4, numero5)
    print("Para la multiplicacion ", resultado2)
    resultado2 = division(numero4, numero5)
    print("Para la division ", resultado2)

    # Para el tercer ejemplo

    print("-----------------------------")
    print("Ejemplo 3")
    print("-----------------------------")
    resultado3 = suma(numero4, numero2)
    print("Para la suma ", resultado3)
    resultado3 = resta(numero4, numero2)
    print("Para la resta ", resultado3)
    resultado3 = multiplicacion(numero4, numero2)
    print("Para la multiplicacion ", resultado3)
    resultado3 = division(numero4, numero2)
    print("Para la division ", resultado3)
