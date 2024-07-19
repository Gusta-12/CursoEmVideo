# Número primo
print('-=-' * 5)
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;32m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('\033[1;32mE por isso ele é PRIMO!\033[m')
else:
    print('\033[1;31mE por isso ele NÃO é PRIMO!\033[m')