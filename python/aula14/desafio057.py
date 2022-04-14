c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[32m'
c3 = '\033[34m'

print('=' * 20, f'{c1}DESAFIO 057{c}', '=' * 20)
sexo = str(input('Sexo [M/F]: ')).strip()
while sexo in 'Mm, Ff' and sexo != '':
    if sexo in 'Mm':
        print('{}Masculino{}'.format(c3, c))
        break
    if sexo in 'Ff':
        print('{}Feminino{}'.format(c3, c))
        break
else:
    print('Digite a opção {}[M]{} ou {}[F]{}.'.format(c2, c, c2, c))

