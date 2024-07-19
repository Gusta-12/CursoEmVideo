# Refazer o ex009, com um número q o usuário escolher
print('-=-' * 5)
s = 0
n = int(input('Escolha um número: '))
for bat in range(0, 11):
    m = n * s
    print('{} x {:2} = {:2}'.format(n, s, m))
    s += 1
print('-=-' * 5)