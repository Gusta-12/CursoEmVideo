def ficha(jog, gol):
    if jog == '':
        jog = '<desconhecido>'
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato!')


n = str(input('Nome do jogador: ')).title()
g = str(input('Qtde de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

ficha(n, g)
