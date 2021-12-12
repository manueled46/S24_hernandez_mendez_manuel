"""
Date: 2021-12-06

Authors: Mauricio Isaias Bolaños Vázquez
        Manuel Yahir Hernandez Mendez
         
File:     T4E1_rock_paper.py

Brief: Utilizando la biblioteca de funciones se juega piedra, papel o tijeras

Score:
    
Version: 0.0.1

Fixes:
"""
import T4E1_rock_paper_functions as rpf

if __name__ == "__main__":
    
    n = 3
    des = []
    print("A continuación jugaremos 3 partidas de piedra, papel o tijera.")
    
    while n > 0:
        us = rpf.seleccion_usuario()
        pc = rpf.seleccion_pc()
        print(f"\nUsted eligio:\n {us}\n")
        print(f'\nYo elegi: \n {pc}\n')
        res = rpf.partida(us, pc)
        des.append(res)
        print("Y el resultado es... \n\n\n", res)
        n -= 1
        
    print("\nLos resultados del juego fueron: ", des)
    
