# Dois números inteiros
print('-=-' * 15)
n1 = int(input('Escolha um número inteiro:'))
n2 = int(input('Escolha outro número inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior!')
    print('Maior: {} \nMenor: {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é maior!')
    print('Maior: {} \nMenor: {}'.format(n2, n1))
else:
    print('Não existe um valor maior, os dois são iguais!')
    print('Primeiro número: {} \nSegundo número: {}'.format(n1, n2))
print('-=-' * 15)