c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 060{c}', '=' * 20)
n = int(input('Digite um número e verás o Calculo do fatorial: '))
c = n
f = 1
print('calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=',  end=' ')
    f *= c
    c -= 1
print('{}'.format(f), end=' ')




