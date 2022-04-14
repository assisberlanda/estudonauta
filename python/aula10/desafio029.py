print('\n', '=' * 30, 'DESAFIO 029', '=' * 30)
carro = int(input('Digite a velocidade do seu carro em Km: '))
vho = '\033[7;31;46m'
vde = '\033[32m'
alo = '\033[33m'
aul = '\033[34m'
rxo = '\033[35m'
cno = '\033[36m'
cza = '\033[37m'
aga = '\033[m'
if carro > 80:
    v = int(carro - 80) * 7
    print('Você ultrapassou a velocidade permitida de {}80km/h!{}, e será multado!'.format(alo, aga))
    print('Você devera pagar uma multa no valor de {}R${:.2f}{}'.format(vho, v, aga))
else:
    print(f'{vde}Dirija com atenção!{aga}')
