from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1 # Torna o passo positivo!
    if passo == 0:
        passo = 1
    print('-=-' * 15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)

    
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True) # Permite q o sleep funcione corretamente
            sleep(.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(.5)
            cont -= passo
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=-' * 15)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
print()
