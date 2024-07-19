from random import randint
print('Vamos jogar impar ou par!')
cont = 0
opc = ''
while True:
    while opc not in 'PI':
        opc = str(input('IMPAR ou PAR ')).upper().strip()[0]
    computador = randint(0, 10)
    jogador = int(input('Escolha um número de 0 a 10: '))
    total = computador + jogador
    print(f'{jogador} + {computador} = {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if opc == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    if opc == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')