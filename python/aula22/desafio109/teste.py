import moeda

p = float(input('Digite o preco R$: '))
t = float(input('Digite uma taxa em %: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando {moeda.moeda(p)} em {t}% é {moeda.aumentar(p, t, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')

