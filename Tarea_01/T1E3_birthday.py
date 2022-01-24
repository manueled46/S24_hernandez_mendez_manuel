"""
Date:     2021-11-22
Authors:  Manuel Yahir Hernandez Mendez
File:     T1E3_birthday.py
Brief:    Este programa solicita año, mes y día de cumpleaños 
          e implime el string 'Year:xxxx - Month:xx - Day: xx'
          con sus respectivos resultados
Score:    80
Version:  1.1.1
Fixes:    - PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','
          
          - Faltaron los dos puntos ':' en el formato de impresion
                solicitado
"""

if __name__ == '__main__':
    a = int(input("Ingrese su año de nacimiento"))
    b = int((input("Ingrese el mes")))
    c = int((input("Dia")))
    print(f"Year: {a} - Month {b} - Day {c}")
    print("Year: {} - Month {} - Day {}".format(a,b,c))
