# Lendo 2 valores
from time import sleep
n1 = int(input('N1: '))
n2 = int(input('N2: '))
esc = 0
while esc != 5:
    print('''MENU
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair''')
    esc = int(input('Opção: '))
    if esc == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        sleep(1)
    elif esc == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
        sleep(1)
    elif esc == 3:
        if n1 > n2:
            print('entre {} e {}, o maior é {}'.format(n1, n2, n1))
            sleep(1)
        elif n2 > n1:
            print('entre {} e {}, o maior é {}'.format(n1, n2, n2))
            sleep(1)
        else:
            print('{} é igual a {}, portanto não há um valor maior!'.format(n1, n2))
            sleep(1)
    elif esc == 4:
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
    elif esc == 5:
        print('FIM DO PROGRAMA')
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')