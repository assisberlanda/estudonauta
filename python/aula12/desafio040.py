

c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 40{}'.format(c1, c), '=' *20)
n1 = float(input('{}Digite a primeira nota: {}'.format(c3, c)))
n2 = float(input('{}Digite a segunda nota: {}'.format(c3, c)))
m = (n1 + n2) / 2
if m <= 7:
    print('Tirando {} e {}, a média do aluno é {}\n{}O aluno está de RECUPERAÇÃO!{}'.format(n1, n2, m, c2, c))
else:
    print('Tirando {} e {}, a média do aluno é {}\n{}O aluno está APROVADO!{}'.format(n1, n2, m, c5, c))
