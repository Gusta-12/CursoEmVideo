def leiaDinheiro(msg):
    valido = False
    while not valido:
        x = str(input(msg)).replace(',', '.').strip()
        if x.isalpha() or x == '':
            print(f'\033[1;31mERRO! \"{x}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(x)
