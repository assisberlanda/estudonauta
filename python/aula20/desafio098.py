from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contando de {i} até {f} de {p} em {p}.')


    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(.3)
            cont += p
        print('FIM')
    else:
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(.3)
            cont -= p
        print('FIM')
contador(0, 10, 1)
contador(10, 0, 1)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)