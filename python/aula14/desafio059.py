c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 059{c}', '=' * 20)
from time import sleep
m = 4
while m == 4:
    n1 = int(input('{}Digite o primeiro número:{} '.format(c3, c)))
    n2 = int(input('{}Digite o segundo número:{} '.format(c2, c)))
    print('--=' * 60)
    print('\n{}[ 1 ] Somar    [ 2 ] Multiplicar    [ 3 ] Maior     [ 4 ] Novos números      [ 5 ] Sair do programa{}'.format(c2, c))
    print('--=' * 60)
    m = int(input('\n{}Digite uma opção acima:{} '.format(c3, c)))
    if m == 1:
        s = n1 + n2
        print('A soma de {} e {} = {}'.format(n1, n2, s))
        break
    if m == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1,n2, n1))
        else:
            print('Entre {} e {} o maior é {}'.format(n1,n2, n2))
        break
    if m == 2:
        s = n1 * n2
        print('O produto de {} e {} = {}'.format(n1, n2, s))
        break
    if m == 5:
        print('{}Finalizando...{}'.format(c3, c))
        sleep(2)
        break
else:
    print('Opcão INVALIDA, escolha de 1 a 5.')



