'''aprovar um emprestimo para comprar uma casa o programa vai perguntar o valor da casa o salario do comrador
e em quantos anos ele vai pagar calcule:

o valor da prestacao mensal em que nao pode exeder 30 % do salario com msg se sera negado ou nao'''

c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 36{}'.format(c1, c), '=' *20)
cas = float(input('{}Qual valor do Imóvel que você quer financiar? R${} '.format(c2, c)))
sal = float(input('{}Quanto é o seu salário? R${} '.format(c2, c)))
tem = int(input('{}Em quanto anos você quer pagar?{} '.format(c2, c)))
pre = cas / (tem * 12)
min = (sal*30/100)
if pre <= min:
    print('{}Parabéns seu empréstimo foi aprovado no valor de R${:.2f}, e você irá pagar uma prestação mensal '
          'no valor de R${:.2f} durante {} anos.{}'.format(c3, cas, pre, tem, c))
else:
    print('{}Desculpe, seu emprestimo foi negado! O valor da prestação ficou R${:.2f}, ultapassando 30% '
          'do seu salário.\nTente pagar em mais tempo!{}'
          '{}Lembrando que você poderá assumir uma prestação de no máximo '
          'R${:.2f}{}.'.format(c4, pre, c, c5, min, c))
# end = ' ' acrescenta a proxima linha na mesma linha anterior