"""
Date: 2021-11/22
Authors: Manuel Yahir Hernandez Mendez
         Mauricio Isaias Bolaños Vázquez
File:     T3E1_return_test.py
Brief: Pedimos un numero y regresamos un string
Score:
Version: 1
Fixes:
"""


def conversion(a):
    a = str(a)
    return a

if __name__ == '__main__':

    numero = 0

    numero = int(input("Digite un numero"))
    Ejemplo = conversion(numero)
    print(numero,type(numero),"\n")
    print(Ejemplo, type(Ejemplo))
