"""
Date: 2021-12-06

Authors: Mauricio Isaias Bolaños Vázquez
        Manuel Yahir Hernandez Mendez
         
File:     T4E1_rock_paper_functions.py

Brief: biblioteca de funciones para el juego piedra, papel o tijeras

Score:
    
Version: 0.0.1

Fixes:
"""

from random import choice

def seleccion_usuario():
    """
    Returns:
    Eleccion hecha por el usuario en el juego piedra, papel o tijera.
    
    su : variable donde se almacena la elección del usuario.

    """
    try:
        list1 = ["piedra", "papel", "tijera"]
        su = int(input("Elija: \n 0 para piedra \n 1 para papel \n 2 para tijera:\n"))
        su = list1[su]
        return su
        
    except:
        print("ingresa un número entre 0, 1 y 2")
    

def seleccion_pc():
    """
    Returns:
    Eleccion hecha por la PC en el juego piedra, papel o tijera.
    sp : variable aleatoria donde se almacena la elección de la PC.

    """
    list1 = ["piedra", "papel", "tijera"]
    sp = choice(list1)
    return sp

def partida(sel1, sel2):
    """
    Parameters
    ----------
    sel1 : Ingresa la elección hecha por el usuario.
    sel2 : Ingresa la elección hecha por la PC.

    Returns
    -------
    result : Regresa si el usuario ganó, perdió o empató.

    """
    
    if sel1 == sel2:
        result = "Empate"
        return result
    
    if sel1 == "piedra" and sel2 == "papel":
        result = "Pierdes"
        return result
        
    elif sel1 == "piedra" and sel2 == "tijera":
        result = "Ganas"
        return result
            
    if sel1 == "papel" and sel2 == "tijera":
        result = "Pierdes"
        return result
        
    elif sel1 == "papel" and sel2 == "piedra":
        result = "Ganas"
        return result
    
    if sel1 == "tijera" and sel2 == "piedra":
        result = "Pierdes"
        return result
        
    elif sel1 == "tijera" and sel2 == "papel":
        result = "Ganas"
        return result
