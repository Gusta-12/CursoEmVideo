# parede
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede possui as dimensões de {} x {} e sua área é de {} m²'.format(larg, alt, area))
tinta = area / 2
# a cada 2 m², se usa 1l de tinta
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tinta))
