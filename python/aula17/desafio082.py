#faça um programa que pede numeros de uma LISTA e mostre, depois mosrtre uma lista para os Pares
    #e uma lista para os Impares.

lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'O total da lista digitada é {lista}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números impares é: {impares}')
