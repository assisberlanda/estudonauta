c = '\033[m'
c1 = '\033[7;40m'
print('\n', '=' *20, f'{c1} DESAFIO 0451 {c}', '=' * 20)
num = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
dec = num + (10-1) * raz
for c in range(num, dec + raz, raz):
    print('{} '.format(c), end=' -> ')
print('Fim')
