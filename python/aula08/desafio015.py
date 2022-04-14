print('==========  Desafio 015  ============')
print('Aluguel carro dia R$60 e R$0,15 por Km rodado.')

dias = int(input('Quantos dias de aluguel? '))
km = int(input('Quantos Km rodado? '))
res = (dias * 60 + km * 0.15)
print(f'Total a pagar é de R${res:.2f}')


