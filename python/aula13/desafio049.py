c = '\033[m'
c1 = '\033[7;40m'
print('\n', '=' *20, f'{c1} DESAFIO 049 {c}', '=' * 20)
from time import sleep
num = int(input('Digite qual tabuada vc quer: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, num * c))
