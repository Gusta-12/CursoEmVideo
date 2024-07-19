boletim = []

while True:
    nome = str(input('Nome: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    
    boletim.append([nome, [n1, n2], media])

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar?[S/N] ')).upper()[0]
    if opc == 'N':
        break

print('-=-' * 15)
print(f'{'No.':<4} {'NOME':<10} {'MÉDIA':>8}')
print('-' * 30)

for i, a in enumerate(boletim):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')

print('-=-' * 15)

while True:
    opc = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break

    if opc <= len(boletim) -1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
    else:
        print('Aluno INVÁLIDO!')
    print('-' * 15)

print('<<< VOLTE SEMPRE >>>')
