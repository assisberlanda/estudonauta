from random import randint
comp = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), )
print('Os valores sorteados foram: ', end='')
for n in comp:
    print(f'{n}', end=' ')
print('\nO maior valor sorteado foi: ', max(comp))
print('O menor valor sorteado foi: ', min(comp))
