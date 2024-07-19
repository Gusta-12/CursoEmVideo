bprec = total = qtde = 0
print('-' * 40)
print(f'{'LOLJA':^40}')
print('-' * 40)
while True:
    nome = str(input('Nome do produto: ')).capitalize().strip()
    prec = float(input('Preço: R$ '))
    total += prec
    if prec > 1000:
        qtde += 1
    if bprec == 0:
        barato = nome
        bprec = prec
    elif bprec > prec:
        barato = nome
        bprec = prec
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if opc == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi de R$ {total:.2f} \nTemos {qtde} produtos custando mais de R$ 1.000,00 \nO produto mais barato foi {barato} que custa R$ {bprec:.2f}')
