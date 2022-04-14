c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 061{c}', '=' * 20)

print('Gerador de PA')
print('--=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} --> '.format(primeiro), end=' ')
    primeiro += razao
    cont += 1
print('Fim')
