def aumentar(num=0, qtde=0):
    x = num + (num * qtde / 100)
    return x


def diminuir(num=0, qtde=0):
    x = num - (num * qtde / 100)
    return x


def dobro(num=0):
    x = num * 2
    return x


def metade(num=0):
    x = num / 2
    return x


def moeda(num=0, moeda='R$'):
    x = f'{moeda} {num:.2f}'.replace('.', ',')
    return x
