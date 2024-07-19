def moeda(num=0, moeda='R$'):
    x = f'{moeda} {num:.2f}'.replace('.', ',')
    return x


def aumentar(num=0, qtde=0, real=False):
    x = num + (num * qtde / 100)
    if real:
        return moeda(x)
    else:
        return x


def diminuir(num=0, qtde=0, real=False):
    x = num - (num * qtde / 100)
    if real:
        return moeda(x)
    else:
        return x


def dobro(num=0, real=False):
    x = num * 2
    if real:
        return moeda(x)
    else:
        return x


def metade(num=0, real=False):
    x = num / 2
    if real:
        return moeda(x)
    else:
        return x
