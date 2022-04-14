n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número: {n[num]:^8}')
        opcao = str(input('Quer continuar [S/N]: ')).strip()
        if opcao in 'Ss':
            continue
        else:
            break
print('Tente novamente...')

