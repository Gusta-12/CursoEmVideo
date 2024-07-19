v = list()
while True:
    v.append(int(input('Digite um valor: ')))
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if opc == 'N':
        break
print('-=-' * 15)
print(f'Foram digitados {len(v)} valores')
v.sort(reverse=True) #SORT não pode ser usado dentro do print (com 'f')
print(f'Valores em ordem decrescente: {v}')
if 5 in v:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')
