c = '\033[m'
c1 = '\033[7;40m'
print('\n', '=' *20, f'{c1} DESAFIO 050 {c}', '=' * 20)

s = 0
c = 0
for n in range(1, 7):
    num = int(input('Digite o Valor {}: '.format(n)))
    if num % 2 == 0:
        s += num
        c += 1
print('Você informou {} números e a soma deles é {}'.format(c, s))

