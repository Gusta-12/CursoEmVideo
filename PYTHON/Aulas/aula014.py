# while
print('-=-' * 10)
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('-=-' * 10)
print('Números PARES: {}\nNúmeros IMPARES: {}'.format(par, impar))
print('-=-' * 10)