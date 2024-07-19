# Peso de cinco pessoas
print('-=-' * 5)
for tab in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(tab)))
    if tab == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('-=-' * 5)
print('Maior peso digitado: {}Kg \nMenor peso digitado: {}Kg'.format(maior, menor))
print('-=-' * 5)