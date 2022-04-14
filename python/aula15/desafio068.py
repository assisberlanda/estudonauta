from random import randint
print('Vamos jogar [Par/Impar]? ')
v = 0
while True:
    jog = int(input('Escolha um número de [1 a 10]: '))
    com = randint(1, 10)
    total = jog + com
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Escolha [ P ] Par ou [ I ] Impar: ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {com}, total de {total}')
    print(f'DEUS PAR' if total % 2 == 0 else 'DEU IMPAR')
    if opcao == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif total == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar Novamente...')
print(f'GAME OVER! Você venceu {v} vezes')
