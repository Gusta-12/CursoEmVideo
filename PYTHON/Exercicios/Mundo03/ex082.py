val = []
impar = []
par = []
while True:
    val.append(int(input('Digite um valor: ')))
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).upper()[0]
    if opc == 'N':
        break
print('-=-' * 15)
print(f'Números digitados: {val}')
for c in val:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Números pares: {par}')
print(f'Números impares: {impar}')