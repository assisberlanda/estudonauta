c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 062{c}', '=' * 20)

print('Gerador de PA')
print('--=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} --> '.format(primeiro), end=' ')
        primeiro += razao
        cont += 1
    print('Pausa...')
    mais = int(input('Quantos termos que mostrar a mais: '))
print('Fim.')