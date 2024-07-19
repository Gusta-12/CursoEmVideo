# Média, maior e menor valor lido
cont = m = 0
c = 'S'
while c != 'N':
    n = int(input('N: '))
    cont += 1
    m += n
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    c = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
print('FIM')
print('Média:', m / cont)
print('Maior: {} \nMenor: {}'.format(maior, menor))