lista = ('Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipisicing',
         'elit', 'Magni', 'iste', 'totam', 'repellendus', 'minus', 'Enim', 'rem', 'tenetur',
         'explicabo', 'Fuga', 'deleniti', 'tempora', 'ea', 'minus', 'fugiat', 'architecto',
         'itaque', 'sed', 'necessitatibus', 'eos', 'earum non')
for p in lista:
    print(f'\nna palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')