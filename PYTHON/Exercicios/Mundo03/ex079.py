valores = []
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('VALOR ADICIONADO com sucesso...')
    else:
        print('VALOR DUPLICADO, irei ignorar...')
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] - ')).upper()[0]
    if r == 'N':
        break
print('-=-' * 15)
valores.sort()
print(f'Os valores digitados foram: {valores }')