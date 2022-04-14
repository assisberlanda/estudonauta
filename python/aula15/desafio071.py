print('=' * 30)
print('{:^30}'.format('BANCO DO ASSIS'))
print('=' * 30)
valor = int(input('Quanto vc quer sacar R$: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} ceduas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break



'''c = 50
v = 20
d = 10
u = 1
c50 = valor // c
c20 = (valor - (c50 * c)) // 20
c10 = (valor - (c50 * c) - (c20 * 20)) // 10
c1 = valor - (c50 * c) - (c20 * 20) - (c10 * 10)
print(f'Total de {c50} de R$ {c}')
print(f'Total de {c20} de R$ {v}')
print(f'Total de {c10} de R$ {d}')
print(f'Total de {c1} de R$ {u}')'''