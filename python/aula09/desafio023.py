print('=' *20, 'DESAFIO 023', '=' *20)
nome = str(input('\nDigite seu nome completo: ')).strip()
print('Seu nome em maiúscula é: {}.'.format(nome.upper()))
print('Seu nome em minúscula é: {}.'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.\n'.format(nome.find(' ')))
print('=' *55)

separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))


