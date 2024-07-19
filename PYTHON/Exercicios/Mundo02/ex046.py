# Contagem regressiva com uma pausa de 1 segundo
from time import sleep
print('-=-' * 15)
print('Atenção para a contagem regressiva dos fogos de artifício!')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('KABOOOOM!')
print('-=-' * 15)