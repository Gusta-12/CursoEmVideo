# Empréstimo
print('-=-' * 15)
casav = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos você vai pagar? '))
por_mes = casav / (tempo * 12)
if por_mes >= sal * 30 / 100:
    print('Empréstimo NEGADO, você teria que pagar R$ {:.2f} por mês.'.format(por_mes))
else:
    print('Empréstimo APROVADO, você pagará R$ {:.2f} por mês durante {} anos.'.format(por_mes, tempo))
print('-=-' * 15)