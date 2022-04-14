from moeda import metade, dobro, aumentar

p = float(input('Digite o preco R$: '))
t = float(input('Digite uma taxa em %: '))
print(f'A metade de R${p:.2f} é R${metade(p):.2f}')
print(f'Aumentando R${p:.2f} em {t:.1f}% é R${aumentar(p, t):.2f}')
print(f'O dobro de R${p:.2f} é R${dobro(p):.2f}')

