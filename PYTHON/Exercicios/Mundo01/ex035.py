# Triângulo (dnv)
l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses valores podem formar um triângulo.')
else:
    print('Esses valores não podem formar um triângulo.')