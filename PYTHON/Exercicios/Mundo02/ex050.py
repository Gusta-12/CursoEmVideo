# Lendo seis números INTEIROS e somando apenas os pares, desconsiderando os valores impares impar
print('-=-' * 5)
s = 0
cont = 0
for atatab in range(1, 7):
    n = int(input('Número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('A soma dos números {} PARES é igual a: {}'.format(cont, s))
print('-=-' * 5)