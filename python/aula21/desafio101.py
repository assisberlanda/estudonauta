def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        return f'Com {idade} anos o Voto é Negado.'
    elif 16 <= idade < 18:
        return f'Com {idade} anos o Voto é Opcional.'
    else:
        return f'Com {idade} anos o Voto é Obrigatorio'


ano = int(input('Ano nascimento: '))
print(voto(ano))