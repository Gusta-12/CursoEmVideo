from random import randint
n = (randint(0, 10), randint(0, 10), 
     randint(0, 10), randint(0, 10), randint(0, 10), )
print('-=-' * 15)
print(f'Os valores sorteados foram: {n}.')
print(f'O maior valor sorteado foi {max(n)}.')
print(f'O menor valor sorteado foi {min(n)}.')
print('-=-' * 15)