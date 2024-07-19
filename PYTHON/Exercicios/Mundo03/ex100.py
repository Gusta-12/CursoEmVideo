from random import randint
from time import sleep

def sorteia(lst):
    print('---' * 15)
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        lst.append(randint(1, 10))
        print(f'{lst[c]}', end=' ', flush=True)
        sleep(.3)
    lst.sort()
    print('PRONTO!')
    sleep(.3)

def somaPar(lst):
    spar = 0
    print('A soma dos valores: ', end='')
    for c in lst:
        if c % 2 == 0:
            print(c, end=' ', flush=True)
            sleep(.3)
            spar += c
    print(f'-> {spar}.')
    sleep(.3)

numeros = []
sorteia(numeros)
somaPar(numeros)
print('---' * 15)
