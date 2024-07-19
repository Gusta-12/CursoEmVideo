from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.7)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)# Ficar do maior para o menor. 1 é pra pegar o valor, e não a chave (lista)
print('---' * 15)
print(' RANKING DOS JOGADORES ')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(.5)
print('---' * 15)