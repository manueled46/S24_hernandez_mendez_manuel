'''
Date: 2021-11/15
Authors: Manuel Yahir Hernandez Mendez
File: main.py
Brief: Este programa utiliza diferentes métodos para listas de numeros
Score:
Version: 1
Fixes:
'''
if __name__ == '__main__':
    lista = ["64","78","43","12","56"]
    inicio = 0;
    fin = 0;
    #Imprimir los elementos y el tipo de lista
    #1
    print("---------------")
    print(lista)
    print(type(lista))
    #Convertir los elementos a int
    #2
    print("---------------")
    lista = list(map(int,lista))
    print(lista)
    #Imprimir un elemento por el usuario
    #3
    print("---------------")
    print("A continuacion digite el rango de la lista que desea ver")
    inicio=int(input("Digite el inicio de la lista"))
    fin=int(input("Digite el final de la lista"))
    print(lista[inicio:fin])
    #Ordenar la lista
    #4
    print("---------------")
    lista.sort()
    print(lista)
    #Ordenar la lista al reves
    #5
    print("---------------")
    lista.sort(reverse= True)
    print(lista)