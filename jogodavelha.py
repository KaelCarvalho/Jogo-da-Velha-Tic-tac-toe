#Jogo da velha 1.0 /Tic-tac-toe game 1.0
#Sujeito a melhorias futuras / May have future implements
#Meu primeiro projeto do curso de python / My first python course project

from IPython.display import clear_output
from random import randint

#Criando a lista que simboliza cada posição do tabuleiro, ignorando o index 0 para melhor gameplay / Creating the board list that symbolizes each board position, ignoring the index 0 for better gameplay
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#Função para mostrar o tabuleiro na tela / Function to print out the board 
def display_tabuleiro(board):
        clear_output()
        print(f''' 
     {board[1]}  | {board[2]}  | {board[3]}
    ____|____|____
     {board[4]}  | {board[5]}  | {board[6]}
    ____|____|____
     {board[7]}  | {board[8]}  | {board[9]} 
        |    |
''')

#Função para limpar o tabuleiro para um novo jogo / Function that clears the board for a new game
def limpar_tabuleiro(lista):
    for item in range(len(lista)):
        if lista[item] == '#':
            pass
        else:
            lista[item] = ' '
    return lista

#Funções de jogadas possíveis para cada jogador / Functions of possibles moves for each player
#Para o jogador 1 / For player 1
def jogada_p1():
    escolha_p1 = 0
    while escolha_p1 not in (1,2,3,4,5,6,7,8,9):
        escolha_p1 = int(input('Vez do Jogador 1: '))
    
    if board[escolha_p1] == ' ':
        board[escolha_p1] = p1
    else:
        escolha_p1 = int(input('Pedido invalido. Tente denovo: '))  
        board[escolha_p1] = p1 
    #Mostra o tabuleiro após cada jogada / Shows the board after each move         
    display_tabuleiro(board)
#Para o jogador 2 / For player 2
def jogada_p2():
    escolha_p2 = 0
    while escolha_p2 not in (1,2,3,4,5,6,7,8,9):
        escolha_p2 = int(input('Vez do Jogador 2:'))

    if board[escolha_p2] == ' ':
        board[escolha_p2] = p2
    else:
        escolha_p2 = int(input('Pedido invalido. Tente denovo: '))
        board[escolha_p2] = p2
    #Mostra o tabuleiro após cada jogada / Shows the board after each move
    display_tabuleiro(board)

#Verifica se alguem ganhou com base em todas as condições de vitória e a 'marca' do jogador (X ou O) / Checks if someone has won using every single win condition and the player 'mark' (X or O)
def ganhou_check(lista,marca):
    return (lista[1]==marca and lista[2]==marca and lista[3]==marca) or (lista[4]==marca and lista[5]==marca and lista[6]==marca) or (lista[7]==marca and lista[8]==marca and lista[9]==marca) or (lista[1]==marca and lista[4]==marca and lista[7]==marca) or (lista[2]==marca and lista[5]==marca and lista[8]==marca) or (lista[9]==marca and lista[6]==marca and lista[3]==marca) or (lista[1]==marca and lista[5]==marca and lista[9]==marca) or (lista[7]==marca and lista[5]==marca and lista[3]==marca)

#Verifica se deu velha / Checks if it is a tie
def velha_check(lista):
    contador_de_casas = 0
    for casa in lista:
        if casa in (('X'),('x'),('O'),('o')):
            contador_de_casas+=1
    if contador_de_casas == 9:
        return True
    else:
        return False

#Definição de laços e condicionais para saber quem começa e se alguem ganhou / Loops and conditionals to know how starts playing and if someone has won
def jogo ():
        if quem_começar == 1:    
            print('Jogador 1 começa')
            while ganhou_check(board,p1) == False and ganhou_check(board,p2) == False and velha_check(board) == False:
                jogada_p1()
                if ganhou_check(board,p1) == True or velha_check(board) == True:
                    break
                
                jogada_p2()
                if ganhou_check(board,p2) == True or velha_check(board) == True:
                    break
        elif quem_começar == 0:
            print('Jogador 2 começa')
            while ganhou_check(board,p1) == False and ganhou_check(board,p2) == False and velha_check(board) == False:
                jogada_p2()
                if ganhou_check(board,p2) == True or velha_check(board) == True:
                    break
                
                jogada_p1()
                if ganhou_check(board,p1) == True or velha_check(board) == True:
                    break

#Tirar na moeda quem começa / Defines how starts
def quem_comeca():
    p1oup2 = randint(0,1)
    return p1oup2

#Meunizinhos para ficar bonito / Displays, maybe someday I'll add english displays..
menu = '''
|=======================|
|     Jogo da Velha     |
|                       |
|   1.Player vs Player  |
|   2.Sair              |
|                       |
|=======================|
'''
menututorial = '''
|=====================================|
|            Como esse jogo           |
|              funciona?              |
|                                     | 
|       Cada número corresponde       |
|      a uma posição do tabuleiro     |
|                                     |
|             1 | 2 | 3               | 
|            ___|___|___              |
|             4 | 5 | 6               |
|            ___|___|___              |
|             7 | 8 | 9               | 
|               |   |                 |  
|                                     | 
|     Escolha um número para marcar   |
|       na posição correspondente     |
|                                     |
|=====================================|
'''

#Parte do código que roda apenas uma vez / Part of the code that runs once
#Definição de variaveis e coisas unicas fora do loop / Variables definitions and unic things outside the loop
p1 = None
p2 = None
print(menu)

sim = ['Sim','sim','s','S']
nao = ['Não','nao','n','N']

#loop
try:
    escolha_menu1 = int(input('Escolha uma opção: '))
    
    while escolha_menu1 == 1 or sim.index(escolha_menu1):
        print(menututorial)
        quem_começar = quem_comeca()
        p1 = None
        p2 = None

        #Definição das marcas / Marks definition
        while p1 not in ('X','x','O','o'):
            p1 = input('Jogador 1, você quer ser X ou O?: ')
        if p1 in ('x','X'):
            p2 = 'O'
        elif p1 in ('O','o'):
            p2 = 'X'
        #Primeira imagem do tabuleiro (vazio) / First board display (empty)
        display_tabuleiro(board)

        #loop interno do jogo /  Internal game loop
        while ganhou_check(board,p1) == False and ganhou_check(board,p2) == False and velha_check(board) == False:
            jogo()
             
        #Finais possíveis para o jogo / Possible endings for the game
        #Jogador um ganha / Player one wins
        if ganhou_check(board,p1) == True:
            print('O Jogador 1 ganhou!! :P')
            limpar_tabuleiro(board)
            
        #Jogador dois ganha / Player two wins
        elif ganhou_check(board,p2) == True:
            print('O Jogador 2 ganhou!! XD')
            limpar_tabuleiro(board)

        #Da velha / Tie
        elif velha_check(board) == True:
            print('A partida deu velha :(')

            limpar_tabuleiro(board)
        
        #Continuar ou parar o loop / Continue or break the loop
        escolha_menu1 = input('Gostaria de jogar de novo?')
        try:
            if sim.index(escolha_menu1):
                continue
        except ValueError:
            if nao.index(escolha_menu1):
                print('Obrigado por jogar!')
                break
#Catch para caso algum erro na entrada / Catch for an error on the input
except ValueError:
    print('Pedido inválido!')