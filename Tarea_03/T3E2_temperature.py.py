"""
Date: 2021-11/22
Authors: Manuel Yahir Hernandez Mendez
File:     T3E2_temperature.py
Brief: Conversiones de unidad de temperatura
Score:
Version: 1
Fixes:
"""


def conversion_c_f(celsius):
    fahe = 0
    CONS1 = 1.8
    CONS2 = 32
    fahe = celsius * CONS1 + CONS2

    return fahe


def conversion_f_c(fahe):
    celsius = 0
    CONS1 = 1.8
    CONS2 = 32
    celsius = (fahe - CONS2) / CONS1

    return celsius


if __name__ == '__main__':
    cels = 0
    fahen = 0
    cels1 = 0
    resultado1 = 0
    resultado2 = 0
    resultado3 = 0

    cels = float(input("Digite una temperatura en celsius"))
    fahen = float(input("Digite una temperatura en fahrenheit"))
    cels1 = float(input("Digite una temperatura en celsius"))

    resultado1 = conversion_c_f(cels)
    print(resultado1)
    resultado1 = conversion_f_c(cels)
    print(resultado1)

    resultado2 = conversion_f_c(fahen)
    print(resultado2)

    resultado3 = conversion_c_f(cels1)
    print(resultado3)
