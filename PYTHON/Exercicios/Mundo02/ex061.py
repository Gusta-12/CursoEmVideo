# PA 2.0
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(p1), end='')
    p1 += r
    cont += 1
print('FIM')
