c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 064{c}', '=' * 20)

n = c = s = 0
n = int(input('Digite um numero [Para parar 999]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um numero [Para parar 999]: '))
print('voce digitou {} entradas e a soma entre elas é {}'.format(c, s))
