c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 43{}'.format(c1, c), '=' *20)
p = float(input('Qual é seu peso? (kg) '))
a = float(input('Qual sua altura? (m) '))
imc = p / (a ** 2)
if imc < 18.5:
    print('O IMC dessa pesso é de {:.1f} e está Abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('O IMC dessa pesso é de {:.1f} e está com Peso Normal.'.format(imc))
elif 25 <= imc < 30:
    print('O IMC dessa pesso é de {:.1f} e está com Sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('O IMC dessa pesso é de {:.1f} e está com Obesidade.'.format(imc))
elif imc >= 40:
    print('O IMC dessa pesso é de {} e está com Obesidade MORBIDA.'.format(imc))
