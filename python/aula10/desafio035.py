print('\n', '=' * 30, 'DESAFIO 035', '=' * 30)
a = int(input('Digite a medida do primeiro lado do Triângulo: '))
b = int(input('Digite a medida do segundo lado do Triângulo: '))
c = int(input('Digite a medida do terceiro lado do Triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('Podemos formar uma triângulo')
else:
    print('Não podemos formar um triângulo')
