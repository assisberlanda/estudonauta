print('\n', '=' *30, 'DESAFIO 027', '=' *30)
nome = str(input('Digite seu nome Completo: ')).strip() .split()
print('Muito prazer em te conhecer {}'.format(nome))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

