print('\n', '=' * 17, 'DESAFIO 026', '=' * 17)
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição: {}'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))
print('=' *49)

