def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: Número a ser calculado.
    :pram show: (opcional) Mostra a conta.
    :return: O valor do fatorial do número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

num = int(input('Núm: '))
opc = ' '
while opc not in 'SN':
    opc = str(input('Deseja ver a conta? [S/N] ')).upper()[0]
if opc == 'S':
    print(fatorial(num, True))
else:
    print(fatorial(num))
print('FIM!')