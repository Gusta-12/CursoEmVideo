def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não escolher um número, \ninterrompendo o sistema...\033[m')
            return 3
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return n


def lin(tam = 40):
    print('\033[1;36m-\033[m' * tam)


def cabecalho(txt='erro'):
    lin()
    print('\033[1;33m', txt.center(40), '\033[m')
    lin()


def menu(lst):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lst:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    lin()
    opc = leiaInt('\033[1;33mSua Opção: \033[m')
    return opc