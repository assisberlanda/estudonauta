'''Faça o Computador jogar jokenpô (Pedra, Papel e Tesoura com vc)'''
from random import randint
from time import sleep
c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 45{}'.format(c1, c), '=' *20)

ite = ('PEDRA', 'PAPEL', 'TESOURA')
com = randint(0, 2)
print('''Suas Opções:
[ 0 ] - PEDRA
[ 1 ] - PAPÉL
[ 2 ] - TESOURA''')
jog = int(input('Qual é a sua Escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print(f'{c3}-={c}' * 20)
print('Computador jogou {} '.format(ite[com]))
print('Você jogou {} '.format(ite[jog]))
print(f'{c3}-={c}' * 20)
if com == 0:
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('Você GANHOU!')
    elif jog == 2:
        print('Computador GANHOU!')
    #elif jog != 0 or jog != 1 or jog != 2:
        #print('Número INVÁLIDO')

elif com == 1:
    if jog == 0:
        print('Computador GANHOU!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('Você GANHOU!')
    #elif jog != 0 or jog != 1 or jog != 2:
     #   print('Número INVÁLIDO')

elif com == 2:
    if jog == 0:
        print('Você GANHOU!')
    elif jog == 1:
        print('Computador GANHOU!')
    elif jog == 2:
        print('EMPATE!')
   # elif jog != 0 or jog != 1 or jog != 2:
        #print('Número INVÁLIDO')
