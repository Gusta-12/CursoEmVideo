# Você acha...
import random
print('Pensando em um número de 0 a 5......')
num = [1, 2, 3, 4, 5]
esc = random.choice(num)
n = int(input('Qual você acha que é o número que eu vou pensar? '))
if n == esc:
    print('Você acertou!')
else:
    print('Você errou, eu estava pensando no número: {}'.format(esc))