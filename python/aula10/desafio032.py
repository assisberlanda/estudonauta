print('\n', '=' * 30, 'DESAFIO 032', '=' * 30)
from datetime import date
ano = int(input('Digite um ano:\nColoque 0 para analizar o ano Atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é bissexto.'.format(ano))
else:
    print('Ano {} não é bissexto'.format(ano))

'''print(f'O ano {ano} é bissexto' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else f'O ano {ano} Não é bissexto')'''



