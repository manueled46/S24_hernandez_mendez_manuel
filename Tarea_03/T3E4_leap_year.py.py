"""
Date: 2021-11/22
Authors: Manuel Yahir Hernandez Mendez
File:    T3E4_leap_year.py
Brief:   Verificar si es una fecha valida
Score:
Version: 1
Fixes:
"""


def verificador(año, mes, dia):
    a = 0
    b = 0
    c = 0
    if año >= 2021:
        a = 1
    if mes > 0 and mes <= 12:
        c = 1
        if mes == 1:
            if dia <= 31:
                b = 1
        elif mes == 2:
            if dia <= 29:
                b = 1
        elif mes == 3:
            if dia <= 31:
                b = 1
        elif mes == 4:
            if dia <= 30:
                b = 1
        elif mes == 5:
            if dia <= 31:
                b = 1
        elif mes == 6:
            if dia <= 30:
                b = 1
        elif mes == 7:
            if dia <= 31:
                b = 1
        elif mes == 8:
            if dia <= 31:
                b = 1
        elif mes == 9:
            if dia <= 30:
                b = 1
        elif mes == 10:
            if dia <= 31:
                b = 1
        elif mes == 11:
            if dia <= 30:
                b = 1
        elif mes == 12:
            if dia <= 31:
                b = 1

    if a == 1 and b == 1 and c == 1:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    year = 0
    month = 0
    day = 0
    year = int(input("Ingrese el año"))
    month = int(input("Ingrese el mes"))
    day = int(input("Ingrese el dia"))

    verificador(year, month, day)
