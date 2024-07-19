from random import randint
from time import sleep
jogos = []
jooj = []
# Introdução
print(f'{'-':-^35}')
print(f'{'JOGA NA MEGA SENA':^35}')
print(f'{'-':-^35}')
# Quantidade de jogos
qtde = int(input('Quantos jogos você quer? '))
print(f'{f' SORTEANDO {qtde} JOGOS ':-^35}')
# Coletando números e colodando na lista principal
for c in range(0, qtde):
    for num in range(0, 6):
        n = randint(1, 60)
        if n not in jooj:
            jooj.append(n)
        else:
            while n in jooj:
                n = randint(1, 60)
            jooj.append(n)
    jooj.sort()
    jogos.append(jooj[:])
    jooj.clear()
# Exibindo jogos
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1:2}: {j}')
    sleep(0.7)
print(f'{'< BOA SORTE! >':-^35}')
