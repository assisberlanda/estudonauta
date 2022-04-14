c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[33m'
c3 = '\033[32m'
print('\n', '=' * 30, '{}DESAFIO 031{}'.format(c1, c), '=' * 30)
v = float(input('{}Digite qual é a distância em km da sua viajem:{} '.format(c2, c)))
if v <= 200:
    p = v * 0.50
elif v > 200 and v < 223:
    p = 100.20
else:
    p = v * 0.45
print('{}O valor de sua passagem será R${:.2f}{}'.format(c3, p, c))


# p = v * 0.50 if v <= 200 else v * 0.45

