# Multa :O
vel = float(input('Em que velocidade o carro esta? '))
mult = vel - 80
if mult <= 0:
    print('Você não foi multado.')
print('Você estava acima do limite de velocidade(80km/h), sua multa será de R$ {:.2f}.'.format(mult * 7.00))