# Alistamento militar
from datetime import date
print('-=-' * 15)
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('-=-' * 15)
print('Quem nasceu em {} terá/tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
print('-=-' * 15)
