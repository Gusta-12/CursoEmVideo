lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: # pega o ÚLTIMO ITEM da lista
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): # do 0 até a ÚLTIMA POSIÇÃO existente na lista
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} na lista...')
                break
            pos += 1
print('-=-' * 15)
print(f'Os valores digitados em ordem foram {lista}')