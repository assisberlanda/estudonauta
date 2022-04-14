c1 = '\033[32m'
c2 = '\033[33m'
c3 = '\033[7;40m'
c = '\033[m'

print('\n', '=' * 30, f'{c3}DESAFIO 034{c}', '=' * 30)
sal = float(input('{}Qual é o seu salário:{} '.format(c2, c)))
if sal <= 1250:
    a1 = sal + sal * 15 / 100
    print('Você receberá um aumento de 15% e seu novo salário será de {}R${:.2f}{}'.format(c2, a1, c))
elif sal > 1250 and sal < 1307:
    sal = 1437.50
    print('Você receberá um aumento e seu novo salário será de {}R${:.2f}{}'.format(c2, sal, c))

else:
    a2 = sal + sal * 10 / 100
    print('Você receberá um aumento de 10% e seu novo salário será de {}R${:.2f}{}'.format(c1, a2, c))
