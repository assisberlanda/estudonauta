c = '\033[m'
c1 = '\033[7;40m'
c2 = '\033[31m'
c3 = '\033[32m'
c4 = '\033[33m'
c5 = '\033[34m'
print('\n', '=' * 20, '{}DESAFIO 37{}'.format(c1, c), '=' *20)

num = int(input('Digite um número: '))
con = int(input('\n{}[ 1 ]-Binário     [ 2 ]-Octal    [ 3 ]-Hexadecimal{}\n\nDigite a opção que você quer converter '
                'o número {}: '.format(c4, c, num)))
if con == 1:
    print('{}O número {} convertido para Binário é: {}{}'.format(c5, num, bin(num)[2:], c))
elif con == 2:
    print('{}O número {} convertido para Octal é: {}{}'.format(c5, num, oct(num)[2:], c))
elif con == 3:
    print('{}O número {} convertido para Octal é: {}{}'.format(c5, num, oct(num)[2:], c))
else:
    print('{}{} é uma opção inválida! Digite a opção 1, 2 ou 3!{}'.format(c3, con, c))

