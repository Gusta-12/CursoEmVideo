def lin():
    print('-' * 22)

def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg} x {comp} é de {a}m².')


print(' Controle de Terrenos ')
lin()
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
lin()
area(l, c)
lin()
