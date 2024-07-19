# Forma de pagamento
print('-=-' * 15)
preco = float(input('Qual o preço do produto? R$ '))
pg = str(input('Qual a forma de pagamento?(dinheiro, cheque, cartão) '))
if pg.lower() == 'dinheiro' or pg.lower() == 'cheque':
    desc = preco - (preco * 10 / 100)
    print('Valor a pagar (COM DESCONTO): R$', desc)
elif pg.lower() == 'cartão' or pg.lower() == 'cartao':
    vezes = int(input('Quantas vezes no cartão? '))
    if vezes == 1:
        desc = preco - (preco * 5 / 100)
        print('Valor a pagar (COM DESCONTO): R$', desc)
    elif vezes == 2:
        print('Valor a pagar: R$ ', preco)
    elif vezes >= 3:
        desc = preco + (preco * 20 / 100)
        print('Valor a pagar (COM JUROS): R$ ', desc)
print('-=-' * 15)