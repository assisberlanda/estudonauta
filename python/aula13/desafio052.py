c = '\033[31m'
c0 = '\033[m'
c1 = '\033[33m'
print('\n', '=' *20, f'{c1} DESAFIO 052 {c0}', '=' * 20)
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if tot == 2:
    print('\n{} é um número PRIMO!'.format(num))
else:
    print('\n{} NÃO é um número PRIMO'.format(num))


