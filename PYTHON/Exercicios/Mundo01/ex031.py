# Viagem
dist = float(input('Qual a distância da viagem(em Km)? '))
if dist <=200:
    val = dist * 0.50
else:
    val = dist * 0.45
print('Você está prestes a fazer uma viagem de {:.1f}Km.'.format(dist))
print('Sua viagem custara: R$ {:.2f}.'.format(val))