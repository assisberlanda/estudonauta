c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 38{}'.format(c1, c), '=' *20)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('{} é maior que {}.'.format(n1, n2))
elif n1 == n2:
    print('OS dois números são iguais.')
elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))


