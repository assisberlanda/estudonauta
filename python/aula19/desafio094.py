galera = []
pessoas = {}
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip() .upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('[ERRO] - Digite M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('[ERRO] - Digite S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoa cadastradas.')
media = soma /  len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
     if p['idade'] >= media:
         print('     ', end='')
         for k, v in p.items():
             print(f'{k} = {v}; ', end='')
         print()
print('«««  ENCERRADO   »»»')