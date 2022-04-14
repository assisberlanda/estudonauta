c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 44{}'.format(c1, c), '=' *20)

print('{:=^50}'.format(' {}LOJAS BERLANDA{} '.format(c5, c)))
mer = float(input('Qual o valor total da compra R$: '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] À vista DINHEIRO
[ 2 ] À vista CARTÃO
[ 3 ] 2X no CARTÃO
[ 4 ] 3X ou mais CARTÃO''')
met = int(input('Digite uma opção de Pagamento acima: {}'.format(c3, c)))
if met == 1:
    avi = mer - (mer * 10 / 100)
    print('Você terá 10% off, e pagará apenas R${:.2f}.'.format(avi))
elif met == 2:
    car = mer - (mer * 5 / 100)
    print('Você terá 5% off, e pagará apenas R${:.2f}.'.format(car))
elif met == 3:
    x2 = mer / 2
    print('Você pagará 2 parcelas de R${:.2f}'.format(x2))
elif met == 4:
    print('Você poderá dividir de 3X a 6X, com 20% de juros.')
    nx = int(input('Em quantas vezes quer dividir: '))
    if 3 <= nx <= 6:
        xn = (mer + (mer * 20 / 100)) / nx
        print('Você pagará em {} parcelas de R${:.2f}'.format(nx, xn))
    elif nx < 3:
        print('{}Volte o Menu e escolha outra opção para melhores condições{}'.format(c5, c))
    else:
        print('{}Não podemos dividir em {} vezes!{}'.format(c4, nx, c))
else:
    print('{} Opção Inválida {}, escolhas opções de {} 1 a 4 {}:'.format(c1, c, c1, c))



