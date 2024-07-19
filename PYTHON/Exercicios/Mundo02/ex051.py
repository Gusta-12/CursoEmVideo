# PA (progressão aritmética)
print('-=-' * 5)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dez = n1 + (10 - 1) * r
for c in range(n1, dez + r, r):
    print(c, end=' -> ')
print('ACABOU!')
print('-=-' * 5)