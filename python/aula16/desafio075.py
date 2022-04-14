num = (int(input('Entre com um numero: ')), int(input('Entre com um numero: ')),
       int(input('Entre com um numero: ')), int(input('Entre com um numero: ')))
print(f'Voce digitou os valore {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 foi digitado na posição: {num.index(3)+1}')
else:
    print('O numero 3 nao foi digitado em nenhuma posição.')
print('os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')

