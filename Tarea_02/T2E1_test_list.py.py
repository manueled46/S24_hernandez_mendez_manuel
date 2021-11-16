'''
Date: 2021-11/15
Authors: Manuel Yahir Hernandez Mendez
File: main.py
Brief: Este programa utiliza diferentes métodos para listas
Score:
Version: 1
Fixes:
'''
if __name__ == '__main__':
    #Creacion de la lista
    lista = ["Calculo","Fisica","Algebra","Humanidades","Qumica"]
    print(lista)
    #Metodo append
    #1
    lista.append("Tutoria")
    print(lista)
    #Metodo inset
    #2
    lista.insert(0,"Bioquimica")
    print(lista)
    #Metodo pop
    #3
    lista.pop(0)
    print(lista)
    #Ordenar mi lista de A-Z
    #4
    lista.sort()
    print(lista)
    #Ordenar mi lista de Z-A
    lista.sort(reverse=True)
    print(lista)
