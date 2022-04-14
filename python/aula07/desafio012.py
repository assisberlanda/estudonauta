print('==========  Desafio 012  ============')

o = str(input('Digite algo que vc quer comprar: '))
v = int(input(f'Quanto custa {o}: R$'))
p = int(input(f'Digite quantos % de desconto você quer ganhar em {o}: '+'%'))
d = (v*p)/100
pf = v-(v*p)/100

print('Com esse desconto de {}%, você vai econominar R${:.2f}, pagando apenas R${:.2f}!'.format(p, d, pf))
