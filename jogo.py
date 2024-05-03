from functions import *
from dicas import *
from sounds import *

difficultySelect = 0
palavra = ""
erros = 0
jogador1Pontuacao = 0
jogador2Pontuacao = 0
clear()

print("""Bem-vindo ao jogo da forca!
Escolha uma opção:
1. Jogar (1 jogador)
2. Jogar (2 jogadores)
3. Palavra personalizada
4. Sair
""")
escolha =  int(input("Digite o número correspondente à opção desejada: "))
clear()
if escolha == 1 or escolha == 2:
    difficultySelect = int(input("""
Deseja escolher qual dificuldade?
1 - Fácil
2 - Difícil
"""))
    clear()
if difficultySelect == 1:
    clear()
    erros = 6
    for index, key in enumerate(easyDifficulty.keys(), 1):
        print(f"{index} - {key}")
    themeSelect = int(input("Selecione um dos temas!"))
    if themeSelect == 1:
        palavra = fruitFunc()
    elif themeSelect == 2:
        palavra = countryFunc()
    elif themeSelect == 3:
        palavra = jobFunc()
    
elif difficultySelect == 2:
    clear()
    erros = 4
    for index, key in enumerate(hardDifficulty.keys(), 1):
        print(f"{index} - {key}")
    themeSelect = int(input("Selecione um dos temas: "))
    if themeSelect == 1:
        palavra = carFunc()
    elif themeSelect == 2:
        palavra = objectFunc()
    elif themeSelect == 3:
        palavra = movieFunc()

if escolha == 1: # 1 player mode
    def main(erros):
        clear()
        letras_certas = ['_'] * len(palavra)
        letras_erradas = []
        dica_usada = False
    
    
        while True:
            if difficultySelect == 1:
                print(mostrar_forca_facil(len(letras_erradas)))
                print('Palavra:', " ".join(letras_certas))
                print('Letras erradas:', " ".join(letras_erradas))
            elif difficultySelect == 2:
                print(mostrar_forca_dificil(len(letras_erradas)))
                print('Palavra:', " ".join(letras_certas))
                print('Letras erradas:', " ".join(letras_erradas))
                
            if all(letra != '_' for letra in letras_certas):
                print(f'Parabéns! Você ganhou!')
                play_win_sound()
                
                break

            if difficultySelect == 2 and not dica_usada and erros == 1:
                dica_opcao = input("Deseja solicitar uma dica? (s/n): ").lower()
                if dica_opcao == 's':
                    print("Dica:", dica(palavra))
                    dica_usada = True
            
            if difficultySelect == 1 and not dica_usada and erros == 3:
                dica_opcao = input("Deseja solicitar uma dica? (s/n): ").lower()
                if dica_opcao == 's':
                    print("Dica:", dica(palavra))
                    dica_usada = True
            palpite = input('Digite uma letra: ').lower()
            
            if len (palpite) != 1 or not palpite.isalpha():
                print('Por favor, digite apenas uma letra válida.')
                continue
            
            if palpite in palavra:
                print('Boa! A letra está na palavra.')
                play_correct_guess_sound()
                for i in range(len(palavra)):
                    if palavra[i] == palpite and i < len(letras_certas):
                        letras_certas[i] = palpite

            else:
                print('Ops! A letra não está na palavra.')
                letras_erradas.append(palpite)
                play_wrong_guess_sound()
                erros -= 1
                
            if  difficultySelect == 1 and erros == 0:
                print(mostrar_forca_facil(6))
                print('Você perdeu! A palavra era: ', palavra)
                play_lose_sound()
                break
            
            if  difficultySelect == 2 and erros == 0:
                print(mostrar_forca_dificil(4))
                print('Você perdeu! A palavra era: ', palavra)
                play_lose_sound()
                break

if escolha == 2: # 2 players mode
    def main(erros):
        clear()
        letras_certas = ['_'] * len(palavra)
        letras_erradas = []
        dica_usada = False
        jogador1Name = input('Qual seu nome, jogador 1? ')
        jogador2Name = input('Qual seu nome, jogador 2? ')
        jogador1Pontuacao = 0
        jogador2Pontuacao = 0
        clear()
    
        while True:
            if erros == 0:
                if difficultySelect == 1:
                    mostrar_forca_facil(len(letras_erradas))
                    print('A palavra era: ', palavra)
                    play_lose_sound()
                    break
                if difficultySelect == 2:
                    mostrar_forca_2Jogadores(len(letras_erradas))
                    print('A palavra era: ', palavra)
                    play_lose_sound()
                    break
            jogador1Ganhou = False
            jogador2Ganhou = False
            jogador1Perdeu = False
            jogador2Perdeu = False
            jogador1 = True
            jogador2 = True

            if difficultySelect == 2 and not dica_usada and erros == 2:
                dica_opcao = input("Deseja solicitar uma dica? (s/n): ").lower()
                if dica_opcao == 's':
                    print("Dica:", dica(palavra))
                    dica_usada = True
            
            if difficultySelect == 1 and not dica_usada and erros == 4:
                dica_opcao = input("Deseja solicitar uma dica? (s/n): ").lower()
                if dica_opcao == 's':
                    print("Dica:", dica(palavra))
                    dica_usada = True

            while jogador1:
                if jogador2Ganhou == False:
                    if all(letra != '_' for letra in letras_certas):
                        print(f'Parabéns {jogador1Name}! Você adivinhou corretamente!')
                        play_correct_guess_sound()
                        jogador1Ganhou = True
                        jogador1Pontuacao += 3
                        print(f'A pontuação do {jogador1Name} foi de {jogador1Pontuacao} pontos!')
                        break

                    if difficultySelect == 1:
                        print(mostrar_forca_facil(len(letras_erradas)))
                        print('Palavra:', " ".join(letras_certas))
                        print('Letras erradas:', " ".join(letras_erradas))
                    elif difficultySelect == 2:
                        print(mostrar_forca_2Jogadores(len(letras_erradas)))
                        print('Palavra:', " ".join(letras_certas))
                        print('Letras erradas:', " ".join(letras_erradas))

                    palpitePlayer1 = input(f'{jogador1Name}, digite uma letra: ').lower()

                    if len(palpitePlayer1) != 1 or not palpitePlayer1.isalpha():
                        print('Por favor, digite apenas uma letra válida.')
                        continue

                    if palpitePlayer1 in palavra:
                        print('Boa! A letra está na palavra.')
                        play_correct_guess_sound()
                        jogador1Pontuacao += 1
                        for i in range(len(palavra)):
                            if palavra[i] == palpitePlayer1 and i < len(letras_certas):
                                letras_certas[i] = palpitePlayer1
                    else:
                        print('Ops! A letra não está na palavra.')
                        play_wrong_guess_sound()
                        letras_erradas.append(palpitePlayer1)
                        erros -= 1
                        break

                    if jogador1Ganhou or jogador1Perdeu:
                        if jogador1Ganhou:
                            print(f'{jogador1Name} ganhou a rodada!')
                            break
                        if jogador1Perdeu:
                            print(f'{jogador1Name} não adivinhou a palavra.')
                            break
                        
            while jogador2:
                if jogador1Ganhou == False:
                    if all(letra != '_' for letra in letras_certas):
                        clear()
                        print(f'Parabéns {jogador2Name}! Você adivinhou corretamente!')
                        play_correct_guess_sound()
                        jogador2Ganhou = True
                        jogador2Pontuacao += 3
                        break

                    if difficultySelect == 1:
                        print(mostrar_forca_facil(len(letras_erradas)))
                        print('Palavra:', " ".join(letras_certas))
                        print('Letras erradas:', " ".join(letras_erradas))
                    elif difficultySelect == 2:
                        print(mostrar_forca_2Jogadores(len(letras_erradas)))
                        print('Palavra:', " ".join(letras_certas))
                        print('Letras erradas:', " ".join(letras_erradas))

                    palpitePlayer2 = input(f'{jogador2Name}, digite uma letra: ').lower()

                    if len(palpitePlayer2) != 1 or not palpitePlayer2.isalpha():
                        print('Por favor, digite apenas uma letra válida.')
                        continue

                    if palpitePlayer2 in palavra:
                        print('Boa! A letra está na palavra.')
                        play_correct_guess_sound()
                        jogador2Pontuacao += 1
                        for i in range(len(palavra)):
                            if palavra[i] == palpitePlayer2 and i < len(letras_certas):
                                letras_certas[i] = palpitePlayer2
                    else:
                        print('Ops! A letra não está na palavra.')
                        play_wrong_guess_sound()
                        letras_erradas.append(palpitePlayer2)
                        erros -= 1
                        break
                    
                    if erros == 0:
                        jogador2Perdeu = True
                        
            if jogador1Ganhou or jogador2Ganhou:
                break
            
            if erros == 0:
                if difficultySelect == 1:
                    print(mostrar_forca_facil(6))
                    print(f'Ninguém acertou a palavra')
                    play_lose_sound()
                    jogador1Perdeu = True
                elif difficultySelect == 2:
                    print(mostrar_forca_dificil(4))
                    print(f'Ninguém acertou a palavra')
                    play_lose_sound()
                    jogador1Perdeu = True
                    
            if jogador1Pontuacao > jogador2Pontuacao:
                print(f"O jogador {jogador1Name} ganhou com {jogador1Pontuacao} pontos!")
            elif jogador2Pontuacao > jogador1Pontuacao:
                print(f"O jogador {jogador2Name} ganhou com {jogador2Pontuacao} pontos!")
            else:
                print(f"Os jogadores {jogador1Name} e {jogador2Name} empataram com {jogador1Pontuacao} pontos!")   

                
if escolha == 3: # custom word mode
    newWord = input('Deseja adicionar qual palavra?')
    def main(erros):
        clear()
        letras_certas = ['_'] * len(newWord)
        letras_erradas = []
        erros = 4

        while True:
            print(mostrar_forca_dificil(len(letras_erradas)))
            print('Palavra:', " ".join(letras_certas))
            print('Letras erradas:', " ".join(letras_erradas))
            
            if all(letra != '_' for letra in letras_certas):
                print(f'Parabéns! Você ganhou!')
                play_win_sound()
                break

            palpite = input('Digite uma letra: ').lower()
            
            if len (palpite) != 1 or not palpite.isalpha():
                print('Por favor, digite apenas uma letra válida.')
                continue
            
            if palpite in newWord:
                print('Boa! A letra está na palavra.')
                play_correct_guess_sound()
                for i in range(len(newWord)):
                    if newWord[i] == palpite and i < len(letras_certas):
                        letras_certas[i] = palpite

            else:
                print('Ops! A letra não está na palavra.')
                letras_erradas.append(palpite)
                play_wrong_guess_sound()
                erros -= 1

            if erros == 0:
                print(mostrar_forca_dificil(4))
                print('Você perdeu! A palavra era: ', newWord)
                play_lose_sound()
                break

if escolha == 4:
    exit()
if __name__ == '__main__':
    while True:
        main(erros)
        again = input('Deseja jogar novamente? (s/n) ').lower()
        if again == 's':
            continue
        elif again == 'n':
            print('Obrigado por jogar!')
            break
        else:
            print('Valor inválido!')