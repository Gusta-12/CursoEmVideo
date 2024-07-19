# Tratando vários valores v2.0
cont = soma = 0
print('Digite 999 para encerrar o programa.')
while True:
    n = int(input('N: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}.')