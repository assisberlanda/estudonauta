lista = ('lapis', 1.45, 'caderno', 9.50, 'mochila', 120, 'lancheira', 40.89, 'tranferidor', 5.80)

print('_' * 40)
print(f'{"LISTA DE MATERIAL":^40}')
print('=' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'{lista[pos]:>7.2f}')
print('~' * 40)