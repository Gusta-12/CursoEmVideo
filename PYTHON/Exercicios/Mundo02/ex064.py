# Tratando de vários números
n = soma = cont = 0
print('Digite 999 para encerrar o programa!')
while n != 999:
    n = int(input('N: '))
    if n != 999:
        cont += 1
        soma += n
print('Quantidade de números digitados:', cont)
print('Soma dos números digitados', soma)
print('FIM')