print('==========  Desafio 011  ============')

print('Calcule a quantidade de tinta que voce vai gastar pra pintar sua parede:')
ap = float(input('Digite a altura da parede em metros: '))
lp = float(input('Digite a largura da parede em metros'))
rt = int(input('Qual o rendimento da tinta em litros/metros²: '))
a = ap*lp
l = a/rt
print('Você tem uma área de {}m² a ser pintada, e irá precisar de {} litros de tinta para pintar sua(s) parede(s)'.format(a,l))
