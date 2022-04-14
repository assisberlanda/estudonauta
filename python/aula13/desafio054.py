c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'
print('\n', '=' *20, f'{c1} DESAFIO 054 {c}', '=' * 20)
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {} Pessoa: '.format(pess)))
    idade = atual - ano
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print('{}A quantidade de pessoas menor é {}{}'.format(c2, menor, c))
print('{}A quantidade de pessoas maior é {}{}'.format(c3, maior, c))

