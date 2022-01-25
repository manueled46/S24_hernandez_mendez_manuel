'''
Date:       2021-11-15
Author:     Manuel Yahir Hernandez Mendez
File:       main.py
Brief:      Este programa utiliza diferentes métodos para listas de
            numeros
Score:      85
Version:    1.1.1
Fixes:      - PEP257 sugiere que los docstrings (como el encabezado)
                deben ir en comillas dobles

            - Las capturas no estaban en el README.md, revisa el PDF
                que les comparti o busca en san Google, un error que
                cometieron tus compañeros es que pusieron la direccion
                de su PC y para que se muestren debe ser la de su
                repositorio

            * Ten cuidado con la creación de archivos revisa la
                diferencia de crear con python file y solo file
                puesto que tienes doble extension .py.py
            
            * Los punto y coma no se usan en este lenguaje, excepeto en 
                los compuestos, pero aun asi no son recomendables. No 
                dan error pero mejor no los uses, podrian confundir a 
                quien lee tu código
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
    inicio = int(input("Digite el inicio de la lista"))
    fin = int(input("Digite el final de la lista"))
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
    
