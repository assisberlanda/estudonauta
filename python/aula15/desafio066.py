con = soma = 0
while True:
    num = int(input('Digite um número [Para parar 999]: '))
    if num == 999:
        break
    con += 1
    soma += num
print(f'Vc digitou {con} números e a soma deles é {soma}.')
