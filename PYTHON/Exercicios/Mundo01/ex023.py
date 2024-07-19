# Milhar, centena, dezena, unidade
num = int(input('Escolha um número de 0 a 9999: '))
#n = str(num)
#print('''Número digitado: {}.
#Unidade: {}
#Dezena: {}
#Centena: {}
#Milhar: {}'''.format(num, n[3], n[2], n[1], n[0]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Seu número é {}. \nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}.'.format(num, u, d, c, m))