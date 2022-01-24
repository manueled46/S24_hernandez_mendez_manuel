"""
Date: 2022-01-23
Author: Manuel Yahir Hernandez Mendez

File:     RedNeuronal
Brief: La primera red neuronal programada
Score:

Version: 0.0.1
Fixes:
"""

import math

class Neuronas():
    #Constructor y atributos
    def __init__(self,entradasIni, entradaPesos, entradasSalidas):
        #Atributos
        self.entrada = entradasIni
        self.pesos = entradaPesos
        self.salidas = entradasSalidas

    #Definición de los métodos  de la clase
    def sumatoria(self):
        """
        Esta funcion hace la sumatoria de las multiplicaciones de las neuronas
        """
        #Variable de suma
        suma = 0.0

        #Ciclo for para sumar todos los valores de entrada
        for inicio in range(0, len(self.entrada)):

            suma += self.entrada[inicio] * self.pesos[inicio]

        return suma

    def FuncionActivacion(self):
        """
        Esta funcion evalua el valor de la sumatoria en una funcion de activacion
        """
        suma = 0.0

        for inicio in range(0, len(self.entrada)):

            suma += self.entrada[inicio] * self.pesos[inicio]

        return 1 / (1 + math.exp(-suma))


if __name__ == '__main__':

    Entradas = [7,21,-10]
    Salidas = [1]
    Pesos = [-2,4.5,8.2,0.5]

    Neurona1 = Neuronas(entradasIni=Entradas, entradaPesos= Pesos, entradasSalidas = Salidas)

    a = 0.0
    b = 0.0

    print(Neurona1.pesos)
    print(Neurona1.entrada)

    a = Neurona1.sumatoria()

    print("El valor para a es")
    print(a)
    print("Por lo que la neurona evaluada en la funcion sigmoide es ")

    b = Neurona1.FuncionActivacion()

    print(b)


