# Refazendo o desafio #035 do triângulos
print('-=-' * 15)
l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses valores formam um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Esses valores não formam um triângulo.')
print('-=-' * 15)
