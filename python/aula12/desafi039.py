c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
from datetime import date

print('\n', '=' * 20, '{}DESAFIO 39{}'.format(c1, c), '=' *20)
atual = date.today().year
nas = int(input('{}Qual o ano que você nasceu:{} '.format(c5, c)))
idade = atual - nas
print('{}Quem nasceu em {} tem {} anos em {}.{}'.format(c4, nas, idade, atual, c ))
if idade == 18:
    print('Você tem que se alistar Imediatamente!')
elif idade < 18:
    ano = 18 - idade
    x = atual + ano
    print('Você só poderá se alistar daqui a {} anos, somente em {}'.format(ano, x))
else:
    atr = nas + 18
    b = atual - atr
    print('Você ja deveria ter se alistado em {} e está {} anos atrasado.'.format(atr, b ))

