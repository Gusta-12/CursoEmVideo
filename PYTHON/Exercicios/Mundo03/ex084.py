dado = []
povo = []
mais = []
menos = []
mai = men = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso(Kg): ')))
    
    if men == 0:
        men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    
    povo.append(dado[:])
    dado.clear()
    
    print('-=-' * 15)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
    print('-=-' * 15)
    if opc == 'N':
        break

for p in povo:
    if p[1] == mai:
        mais.append(p[0])
    elif p[1] == men:
        menos.append(p[0])

print(f'Foram cadastradas {len(povo)} pessoas.')
print(f'O maior peso foi de {mai:.1f}Kg. Peso de: {mais}')
print(f'O menor peso foi de {men:.1f}Kg. Peso de: {menos}')
print('-=-' * 15)