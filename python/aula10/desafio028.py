from random import randint
from time import sleep
vho = '\033[31m'
vde = '\033[32m'
alo = '\033[33m'
aul = '\033[34m'
rxo = '\033[35m'
cno = '\033[36m'
cza = '\033[37m'
aga = '\033[m'
print('\n', '=' * 30, f'{vho}DESAFIO 028{aga}', '=' * 30)
print(f'{alo}=--{aga}' * 47)
print('{}Vou pensar em um número de 0 a 5. tente adivinhar...{}'.format(aul, aga))
print(f'{alo}=--{aga}' * 47)
comp = randint(0, 5)
n = int(input('{}Em que número eu pensei?{} '.format(vde, aga)))
print('Processando...')
sleep(2)
if n == comp:
    print(f'Parabém você acertou!!! Eu realmente pensei no número {comp}')
else:
    print(f'Você acha que eu pensei no {n}, você está enganado meu chapa!')
    sleep(3)
    print('Eu pensei no {}, e não no {}. Tente novamente:'.format(comp, n))

