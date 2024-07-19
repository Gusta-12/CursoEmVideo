estenso = ('zero', 'um', 'dois', 'três', 'quatro', 
           'cinco', 'seis', 'sete', 'oito', 'nove', 
           'dez', 'onze', 'doze', 'treze', 'quartorze', 
           'quinze', 'dezesseis', 'dezessete', 
           'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        esc = int(input('Escolha um número de 0 a 20: '))
        if 0 <= esc <= 20:
            break
        print('Tente novamente! ', end='')
    print(f'Você digitou o número {estenso[esc]}.')
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if opc == 'N':
        break
print('FIM')