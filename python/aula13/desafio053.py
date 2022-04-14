c = '\033[m'
c1 = '\033[7;40m'
print('\n', '=' *20, f'{c1} DESAFIO 053 {c}', '=' * 20)
frase = str(input('Digite um frase: ')).strip() .upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('São PALÍNDROMO.')
else:
    print('Não temos Palíndromo')