from random import randint
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = []
print('valores sorteados:')
for k, v in jogo.items():
    print(f'{k}tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')