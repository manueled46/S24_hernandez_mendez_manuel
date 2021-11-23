"""
Date: 2021-11/22
Authors: Manuel Yahir Hernandez Mendez
         Mauricio Isaias Bolaños Vázquez
File:     T3E3_arithmetic.py
Brief:   Operaciones de numeros flotantes
Score:
Version: 0.0.1
Fixes:
"""
def suma(a, b):
    res = a + b
    return res

def resta(a, b):
    res = a - b
    return res

def multiplicacion(a, b):
    res = a * b
    return res

def division(a, b):
    res = a / b
    return res


if __name__ == '__main__':
    NUM1 = 1
    NUM2 = 5
    NUM4 = 7
    NUM5 = 9
    # para el PRIMER ejemplo

    resultado1 = suma(NUM1, NUM5)
    print("Para la suma ", resultado1)
    resultado1 = resta(NUM1, NUM5)
    print("Para la resta ", resultado1)
    resultado1 = multiplicacion(NUM1, NUM5)
    print("Para la multiplicacion ", resultado1)
    resultado1 = division(NUM1, NUM5)
    print("Para la division ", resultado1)

    # Para el segundo ejemplo

    print("-----------------------------")
    print("Ejemplo 2")
    print("-----------------------------")
    resultado2 = suma(NUM4, NUM5)

    print("Para la suma ", resultado2)
    resultado2 = resta(NUM4, NUM5)
    print("Para la resta ", resultado2)
    resultado2 = multiplicacion(NUM4, NUM5)
    print("Para la multiplicacion ", resultado2)
    resultado2 = division(NUM4, NUM5)
    print("Para la division ", resultado2)
