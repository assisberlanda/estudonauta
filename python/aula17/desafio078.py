lista = list()
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O MAIOR número digitado foi: {maior}, nas posições: ')
print(f'O MENOR número digitado foi: {menor}, nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...')
print('=' * 30)
print(f'Você digitou os valores {lista}')
