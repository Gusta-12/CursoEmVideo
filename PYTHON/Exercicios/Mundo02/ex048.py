# Soma dos números múltiplos de 3 entre 1 e 500
s = 0
cont = 0
for atatab in range (3, 501, 2):
    if atatab % 3 == 0:
        cont += 1
        s += atatab
print('Quantidade números múltiplos de três: {}\nValor da soma entre eles: {}'.format(cont,s))