col = ('Maria', 'Joao', 'Marcio', 'Alfredo', 'Sergio', 'Paulo', 'Pedro', 'Marcos',
       'Serguei', 'Tadeu', 'Tiburcio', 'Gonofredo', 'Espirrando', 'Fernando', 'Pacheco',
       'Balbucio', 'Tereza', 'Cipreste', 'Severino', 'Cheiroso')
print('--=' * 15)
print('A) Os 5 primeiros são: ', col[:5])
print('--=' * 15)
print('B) Os 4 últimos são: ', col[-4:])
print('--=' * 15)
print('C) Os cinco primeiros são: ', sorted(col))
print('--=' * 15)
print('D) Marcos está na posição: ', col.index('Marcos')+1)
print('--=' * 15)
