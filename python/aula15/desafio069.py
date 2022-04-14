maior = homem = mulher = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade >= 18:
        maior += 1
    if sexo in 'M':
        homem += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        print('-' * 30)
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres menores de 20 anos: {mulher}')
