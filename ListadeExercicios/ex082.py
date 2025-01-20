from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
jogo["Jogador 1"] = randint(1, 6)
jogo["Jogador 2"] = randint(1, 6)
jogo["Jogador 3"] = randint(1, 6)
jogo["Jogador 4"] = randint(1, 6)
ranking = list()
for k, v in jogo.items():
    print(f'O {k} tirou: {v}')
    sleep(0.5)
print("Ranking")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)
