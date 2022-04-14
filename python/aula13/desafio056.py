c = '\033[m'
c1 = '\033[7;40m'
print('\n', '=' * 20, f'{c1} DESAFIO 056 {c}', '=' * 20)
sidade = 0
midade = 0
ihmv = 0
nhmv = ''
mmva = 0
for pes in range(1, 5):
    print('----- {} PESSOA -----'.format(pes))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if sexo in 'Mm' and idade > ihmv:
        ihmv = idade
        nhmv = nome
    if sexo in 'Ff' and idade < 20:
        mmva += 1
midade = sidade / 4
print('A média de idade é {}'.format(midade))
print('A idade do Homem mais velho é {} e o nome dele é {}'.format(ihmv, nhmv))
print('Existe {} mulheres menores que 20 anos'.format(mmva))


'''    if pes == 1 and sexo in 'Mm':
        ihmv = idade
        nhmv = nome'''