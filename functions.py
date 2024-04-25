import random
import os
from dicionario import *

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def fruitFunc():
    return random.choice(frutas)

def countryFunc():
    return random.choice(paises)

def jobFunc():
    return random.choice(profissoes)

def carFunc():
    return random.choice(carros)

def objectFunc():
    return random.choice(objetos)

def movieFunc():
    return random.choice(filmes)

def mostrar_forca_facil(erros):
    forca = [
        """
           ------
           |    |
           |
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |    |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |   /|
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |   /|\\
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |   /|\\
           |    |
           |   /
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |   /|\\
           |    |
           |   / \\
        """
    ]
    return forca[erros]

def mostrar_forca_dificil(erros):
    forca = [
        """
           ------
           |    |
           |
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |   /|\\
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |   /|\\
           |    |
           |   / \\
        _________
        """
    ]
    if erros < 0:
        erros = 0
    elif erros >= len(forca):
        erros = len(forca) - 1
    
    return forca[erros]

def mostrar_forca_2Jogadores(erros):
    forca = [
        """
           ------
           |    |
           |
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |    |
           |    |
           |
        ---------
        """,
        """
           ------
           |    |
           |    ○
           |   /|\\
           |    |
           |
        _________
        """,
        """
           ------
           |    |
           |    ○
           |   /|\\
           |    |
           |   / \\
        _________
        """
    ]
    if erros < 0:
        erros = 0
    elif erros >= len(forca):
        erros = len(forca) - 1
    
    return forca[erros]
