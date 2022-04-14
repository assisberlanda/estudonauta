c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 41{}'.format(c1, c), '=' *20)
from datetime import date
'''ate 9 mirim
ate 14 infantil
ate 19 junior
ate 25 senior
acima master'''
ano = int(input('Digite o ano que voce nasceu com 4 digitos: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos de idade e \nSua Classificação é {}Mirim{}'.format(idade, c2, c))
elif 9 < idade <=14:
    print('Você tem {} anos de idade e \nSua Classificação é {}Infantil{}'.format(idade, c2, c))
elif 14 < idade <= 19:
    print('Você tem {} anos de idade e \nSua Classificação é {}Júnior{}'.format(idade, c2, c))
elif 19 < idade <=25:
    print('Você tem {} anos de idade e \nSua Classificação é {}Senior{}'.format(idade, c2, c))
else:
    print('Você tem {} anos de idade e \nSua Classificação é {}Master{}'.format(idade, c2, c))

