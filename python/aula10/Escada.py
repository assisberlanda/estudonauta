print('\n', '--=' * 10, 'MONTAGEM DA ESCADA', '--=' * 10)
degraus = int(input('Digite a quantidade de degraus da escada: '))
n = 0
fixo = degraus
s ='*'
v = ' '
s1 = s
while n < degraus:
    print(v * fixo, s, '\n')
    n = n + 1
    fixo = fixo - 1
    s = s + s1


