from time import sleep
def maior(*num):
    print('-=-' * 15)
    if len(num) == 0:
        print('Não foi informado nenhum valor.')
        sleep(.5)
        print('Não há valores para analisar...')
        sleep(.5)
    else:
        cont = maior = 0
        print('Analisando os valores passados...')
        for c in num:
            print(c, end=' ', flush=True)
            sleep(.5)
            if cont == 0:
                maior = c
                cont += 1
            elif c > maior:
                maior = c
        print(f'Foram informados {len(num)} valores ao todo.')
        sleep(.5)
        print(f'O maior valor informado foi {maior}')
        sleep(.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print()
