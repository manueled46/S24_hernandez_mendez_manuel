"""
Date: 2021-11/22
Authors: Manuel Yahir Hernandez Mendez
         Mauricio Isaias Bolaños Vázquez
File:     T3E2_temperature.py
Brief: Conversiones de unidad de temperatura
Score:
Version: 0.0.1
Fixes:
"""

def conversion_c_f(celsius):
    CONS1 = 1.8
    CONS2 = 32
    fahe = celsius * CONS1 + CONS2

    return fahe


def conversion_f_c(fahe):
    CONS1 = 1.8
    CONS2 = 32
    celsius = (fahe - CONS2) / CONS1

    return celsius

if __name__ == "__main__":
    
    #Conversiones celsius a fahrenheit
    TC1 = float(input("Digite una temperatura en celsius: "))
    TC2 = float(input("Digite una temperatura en celsius: "))
    TC3 = float(input("Digite una temperatura en celsius: "))

    resultado = conversion_c_f(TC1)
    print(resultado)
    resultado1 = conversion_c_f(TC2)
    print(resultado1)
    resultado2 = conversion_c_f(TC3)
    print(resultado2)
    
    #Conversiones fahrenheit a celsius
    TF1 = float(input("Digite una temperatura en fahrenheit: "))
    TF2 = float(input("Digite una temperatura en fahrenheit: "))
    TF3 = float(input("Digite una temperatura en fahrenheit: "))
    
    R1 = conversion_f_c(TF1)
    print(R1)
    R2 = conversion_f_c(TF2)
    print(R2)
    R3 = conversion_f_c(TF3)
    print(R3)
