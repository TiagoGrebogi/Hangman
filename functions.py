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
    
    return forca[erros]

