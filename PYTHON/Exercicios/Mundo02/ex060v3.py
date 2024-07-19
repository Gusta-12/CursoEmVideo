# Fatorial v3
n = int(input('Digite um número para calcular seu FATORIAL: '))
c = n
f = 1
print('{}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))