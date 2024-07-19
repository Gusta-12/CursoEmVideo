qtde18 = qtdeM = qtdeF20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ')).upper().strip()[0]
    if idade >= 18:
        qtde18 += 1
    if sexo == 'M':
        qtdeM += 1
    if sexo == 'F' and idade < 20:
        qtdeF20 += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if opc == 'N':
        break
print('~' * 20)
print(f'Quantidade de pessoas com mais de 18 anos: {qtde18}; \nQuantidade de homens cadastrados: {qtdeM}; \nQuantidade de mulheres com menos de 20 anos: {qtdeF20}')
print('FIM')
print('~' * 20)