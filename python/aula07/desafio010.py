print('==========  Desafio 010  ============')
#considerando o US$1.00 = R$5,27
print('Conversor de Real/Dolar')
d = 5.27
r = int(input('Quantos R$ você quer converter? '))
c = r/d
print('R${} real(s), equivale a US${} dolares na cotação de Hoje!'.format(r, c))
