lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
# TUPLAS são imutáveis!!!!
print(lanche)
print('-' * 5)
print('[0]', lanche[0])
print('[1]', lanche[1])
print('[2]', lanche[2])
print('[3]', lanche[3])
print('-' * 5)
#for comida in lanche:
for pos, comida, in enumerate(lanche):
    print(f'{comida} na posição {pos}')
#for cont in range(0, len(lanche)):
#    print(lanche[cont])