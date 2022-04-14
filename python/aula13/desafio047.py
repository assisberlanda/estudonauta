
c = '\033[m'
c1 = '\033[7;40m'
print('\n', '=' *20, f'{c1} DESAFIO 047 {c}', '=' * 20)

n = int(input('Digite um número de 1 - 1000: '))
print('''[ 1 ] - Listar Números Pares
[ 2 ] - Listar Números Impares)''')
op = int(input('Digite uma opção acima: '))
if op == 1:
    for c in range(0, n+1, 2):
        print(c, end=' ')
elif op == 2:
    for c in range(0+1, n, 2):
        print(c, end=' ')
else:
    print('Opção INVÁLIDA!!')
'''for n in range(2, 51, 2):
    print(n, end=' ')
print('fim')'''