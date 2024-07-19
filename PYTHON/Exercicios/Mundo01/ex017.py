# Catetos, e Hipotenuza
'''c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
h = (c1 ** 2 + c2 ** 2) ** (1/2)
print('O valor da hipotenusa é de {:.2f}.'.format(h))'''

from math import hypot
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
h = hypot(c1, c2)
print('O valor da hipotenusa é de {:.2f}.'.format(h))
