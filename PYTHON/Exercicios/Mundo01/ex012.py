# Descontão
valor = float(input('Qual o valor do  produto? R$ '))
desc = valor - (valor * 5 / 100)
print('O valor do produto é de R$ {}\nQue com desconto sai por R$ {:.2f}'.format(valor, desc))
