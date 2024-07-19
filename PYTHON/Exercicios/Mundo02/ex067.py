while True:
    n = int(input('Deseja ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c:4}')
print('Programa ENCERRADO com sucesso, volte sempre!')