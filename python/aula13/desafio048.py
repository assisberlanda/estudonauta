c = '\033[m'
c1 = '\033[34m'
print('{:=^50}'.format( f' {c1}Desafio 048{c} '))
s = 0
q = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        q += 1
print('A soma de todos os {} números é {}'.format(q, s), end=' ')


