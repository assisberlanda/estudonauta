from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário R$: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratacao'] + 35) - date.today().year
print('-=' * 30)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')