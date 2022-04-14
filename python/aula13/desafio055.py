c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'
print('\n', '=' *20, f'{c1} DESAFIO 055 {c}', '=' * 20)
maior = 0
menor = 0
for pes in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(pes)))
    if pes == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{}O maior peso é {}Kg.{}'.format(c2, maior, c))
print('{}O menor peso é {}Kg.{}'.format(c3, menor, c))
