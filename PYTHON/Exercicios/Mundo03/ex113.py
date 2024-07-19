def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        except:
            print('\033[1;31mERRO! Digite um número Inteiro válido!\033[m')
            continue # Joga pro while dnv
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        except:
            print('\033[1;31mERRO! Digite um número Real válido!\033[m')
        else:
            return n



i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {i} e o Real foi {r}')