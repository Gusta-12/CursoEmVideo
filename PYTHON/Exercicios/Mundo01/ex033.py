# Maior e menor
a = float(input('Escolha o primeiro número: '))
b = float(input('Escolha o segundo número: '))
c = float(input('Escolha o terceiro número: '))
if a > b and a > c and c > b:
    print('Maior: {:.2f} \nMenor: {:.2f}'.format(a,b))
if b > a and b > c and c > a:
    print('Maior: {:.2f} \nMenor: {:.2f}'.format(b,a))
if c > a and c > b and a > b:
    print('Maior: {:.2f} \nMenor: {:.2f}'.format(c,b))
if c > a and c > b and b > a:
    print('Maior: {:.2f} \nMenor: {:.2f}'.format(c,a))
if a > c and a > b and b > c:
    print('Maior: {:.2f} \nMenor: {:.2f}'.format(a,c))
if b > a and b > c and a > c:
    print('Maior: {:.2f} \nMenor: {:.2f}'.format(b,c))
