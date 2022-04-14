lista = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break

lista.sort(reverse=True)
print(f'Voce digitou {len(lista)} elementos')


