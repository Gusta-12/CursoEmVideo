# Parâmetros Opcionais
def somar(a=0, b=0, c=0): # Se não receber um valor C, ele irá valer 0
    """
    -> Faz a soma de até três valores, e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'{a} + {b} + {c} = {s}')


somar(3, 2, 5)
somar(8, 4)
somar()