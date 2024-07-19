# Categoria do atleta de natação(idade)
from datetime import date
print('-=-' * 15)
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('Idade:', idade)
if idade <= 9:
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JUNIOR.')
elif idade <= 25:
    print('Categoria: SENIOR.')
else:
    print('Categoria: MASTER.')
print('-=-' * 15)