from Auteis22A import numeros
#    PACOTE         PACOTE/MÓDULO
while True:
    num = int(input('Núm: '))
    fat = numeros.fatorial(num)
    print(f'O fatorial de {num} é {fat}')
    print(f'O dobro de {num} é {numeros.dobro(num)}')
    print(f'O triplo de {num} é {numeros.triplo(num)}')
    if num == 0:
        break
