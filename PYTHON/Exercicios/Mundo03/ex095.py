time = []
jogador = {}
partidas = []

while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    tot = int(input('Partidas jogadas: '))

    for c in range(0, tot):
        partidas.append(int(input(f'  Gols na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())
    jogador.clear()
    partidas.clear()

    opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while opc not in 'SN':
        print('ERRO! Responda apenas S ou N')
        opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
    
    if opc == 'N':
        break
print('-=-' * 15)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}')

print('---' * 15)

for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para) '))
    
    if busca == 999:
        break
    
    if busca >= len(time):
        print(f'ERRO! não existe jogador com código {busca}!')
    
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    
    print('---' * 15)
print('FIM')