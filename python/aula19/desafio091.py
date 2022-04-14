from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogodar 1':randint(1, 6),
        'jogodar 2':randint(1, 6),
        'jogodar 3':randint(1, 6),
        'jogodar 4':randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'Jogador {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('  ====   RANKING DOS JOGADORES   ====')
for i, v in enumerate(ranking):
    print(f'{i+1}o. lugar: {v[0]} tirou {v[1]} no dado.')
    sleep(1)

