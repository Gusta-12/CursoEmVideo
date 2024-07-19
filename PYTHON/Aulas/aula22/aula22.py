import uteis
while True:
    num = int(input('Núm: '))
    fat = uteis.fatorial(num)
    print(f'O fatorial de {num} é {fat}')
    print(f'O dobro de {num} é {uteis.dobro(num)}')
    print(f'O triplo de {num} é {uteis.triplo(num)}')
    if num == 0:
        break
