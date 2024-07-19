def moeda(num=0, moeda='R$'):
    x = f'{moeda} {num:.2f}'.replace('.', ',')
    return x


def aumentar(num=0, qtde=0):
    x = num + (num * qtde / 100)
    return moeda(x)


def diminuir(num=0, qtde=0):
    x = num - (num * qtde / 100)
    return moeda(x)


def dobro(num=0):
    x = num * 2
    return moeda(x)


def metade(num=0):
    x = num / 2
    return moeda(x)


def resumo(num=0, porc1=0, porc2=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num)}')
    print(f'Metade do preço: \t{metade(num)}')
    print(f'{porc1}% de aumento: \t{aumentar(num, porc1)}')
    print(f'{porc2}% de redução: \t{diminuir(num, porc2)}')
    print('-' * 30)
