c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 063{c}', '=' * 20)
print('~-~-' *15)
print('SEQUENCIA DE FIBONACCI')
print('~-~-' *15)
ter = int(input('Quantos termos quer mostrar: '))
t1 = 0
t2 = 1
con = 3
print('{} -> {} ', end="".format(t1, t1))
while con <= ter:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    con += 1
print(' -> FIM!')
