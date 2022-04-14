total = pmm = menor = cont = 0
pmb = ' '
while True:
    prod = str(input('Qual o nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        pmm += 1
    if cont == 1 or preco < menor:
        menor = preco
        pmb = prod
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total:5.2f}')
print(f'A quantidade de produto mais que R$ 1000 foi R$ {pmm}')
print(f'E o produto mais barato foi {pmb} e custou R$ {menor:.2f}')


