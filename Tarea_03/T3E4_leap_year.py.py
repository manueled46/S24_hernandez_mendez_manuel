"""
Date: 2021-11/22
Authors: Manuel Yahir Hernandez Mendez
         Mauricio Isaias Bolaños Vázquez
File:    T3E4_leap_year.py
Brief:   Verificar si es una fecha valida
Score:
Version: 0.0.1
Fixes:
"""


def verificador(año, mes, dia):
    #fechas futuras y meses que no existen
    if año > 2021 or mes > 12:
        return False
    
    #febrero y año bisiesto

    P1 = año % 4
    P2 = año % 100
    P3 = año % 400

    if dia <= 29 and mes == 2:
        if P1 != 0:
            return False
        if P1 == 0 and P2 != 0:
            return True
        if P1 == 0 and P2 == 0 and P3 != 0:
            return False
        if P1 == 0 and P2 == 0 and P3 == 0:
            return True
   
    #meses con 30 dias
         
    if mes == 4 or 6 or 9 or 11:
        if dia > 30:
            return False
        else:
            return True
    
    #meses con 31 dias
         
    if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if dia > 31:
            return False
        else:
            return True
    

if __name__ == '__main__':
    
    year = int(input("Ingrese el año: "))
    month = int(input("Ingrese el mes: "))
    day = int(input("Ingrese el dia: "))

    print("\n", verificador(year, month, day))
