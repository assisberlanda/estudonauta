c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 058{c}', '=' * 20)
from random import randint
com = randint(0, 10)
pal = 0
nesc = -1
print('Tente adivinhar o número que estou pensando de [1 a 10]: ')
while nesc < com:
    num = int(input('Digite o numero: '))
    pal += 1
    if num == com:
        print('PARABÉNS, você acertou! Eu pensei no número {}'.format(com))
        print('Você tentou {}X para acertar.'.format(pal))
        break
    else:
        if num < com:
            print('Mais... Tente novamete!')
        else:
            print('Menos... Tente novamete!')




