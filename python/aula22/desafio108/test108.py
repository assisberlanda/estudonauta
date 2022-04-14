import moeda

p = float(input('Digite o preco R$: '))
t = float(input('Digite uma taxa em %: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando {moeda.moeda(p)} em {t}% é {moeda.moeda(moeda.aumentar(p, t))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')

