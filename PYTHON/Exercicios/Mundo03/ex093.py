dados = {}
partidas = []

dados['nome'] = str(input('Nome do Jogador: ')).capitalize()
tot = int(input('Partidas jogadas: '))

for c in range(0, tot):
    partidas.append(int(input(f'  Gols na partida {c + 1}: ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)

print('-=-' * 15)
print(dados)
print('-=-' * 15)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 15)

print(f'O jogador {dados['nome']} jogou {tot} partidas.')
for p, g in enumerate(dados['gols']):
    print(f'  => Na partida {p + 1} fez {g} gol(s).')
print(f'Foi um total de {dados["total"]} gols!')