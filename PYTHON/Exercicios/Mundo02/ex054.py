# Quantos maiores, e quantos menores
from datetime import date
ano = date.today().year
maior = 0
menor = 0
print('-=-' * 15)
for ta in range(1, 7 + 1):
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(ta)))
    if ano - nasc < 21:
        menor += 1
    else:
        maior += 1
print('-=-' * 15)
print('Pessoas de maior: {}\nPessoas de menor: {}'.format(maior, menor))
print('-=-' * 15)