print('{:=^50}'.format( ' Desafio 046 '))

from time import sleep
print('Contagem regressiva para estouro de fogos: ')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOOMMM!!')


