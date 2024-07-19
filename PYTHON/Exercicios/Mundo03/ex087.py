matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mai = 0
# Preenchendo a Matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))

print('-=-' * 15)
# Exibindo a Matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
# Coletando dados da Matriz
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

for l in range(0,3):
    scol += matriz[l][2]

for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print('-=-' * 15)
# Exibindo os dados da Matriz
print(f'A soma de todos os valores PARES é igual a {spar}.')
print(f'A soma dos números da terceira coluna é {scol}.')
print(f'O maior número da segunda linha é {mai}')