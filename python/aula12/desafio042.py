c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 42{}'.format(c1, c), '=' *20)
a = int(input('digite o primeiro seguimento: '))
b = int(input('digite o segundo seguimento: '))
c = int(input('digite o terceiro seguimento: '))

if a < b + c and b < a + c and c < a + b:
    print('podem formar um Triangulo ', end='')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isoceles')


else:
    print('Não podem formar um triângulo!')
