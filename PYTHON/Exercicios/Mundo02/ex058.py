# Adivinhação 2.0
from random import randint
from time import sleep
cores = {'limpa' : '\033[m',
         'padrao' : '\033[1m',
         'errou' : '\033[1;31m',
         'acertou' : '\033[1;32m'}
computador = randint(0, 10)
print('{}Vou escolher um número de 0 a 10, tente adivinhar!'.format(cores['padrao']))
acertou = False
cont = 0
while not acertou:
    jogador = int(input('{}Qual número eu escolhi? '.format(cores['padrao'])))
    cont += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('{}Você errou!{} {}Tente um número maior...{}'.format(cores['errou'], cores['limpa'], cores['padrao'], cores['limpa']))
        sleep(0.5)
    else:
        print('{}Você errou!{} {}Tente um número menor...{}'.format(cores['errou'], cores['limpa'], cores['padrao'], cores['limpa']))
        sleep(0.5)
if cont == 1:
    print('{}PARABÉNS! Você acertou de primeira! :O{}'.format(cores['acertou'], cores['limpa']))
else:
    print('{}Você acertou!{} {}Com {} tentativas.{}'.format(cores['acertou'], cores['limpa'], cores['padrao'], cont, cores['limpa']))
print('{}FIM{}'.format(cores['padrao'], cores['limpa']))
