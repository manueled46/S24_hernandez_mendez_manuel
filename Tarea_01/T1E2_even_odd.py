"""
Date:       2021-10-31
Author:     Manuel Yahir Hernández Méndez
File:       T1E2_even_odd.py
Brief:      Ingresar un número y validar si es par o impar
Score:      100
Version:    1.1.1
Fixes:      -
"""

if __name__ == '__main__':
    a = int(input("Ingrese un numero"))
    # Seria bueno validar e indicar cuando el número es cero
    if a % 2 == 0:
        print("El numero es par")
    else:
        print("Es impar")
