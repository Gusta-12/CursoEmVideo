# Carros Alugados
dia = float(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pagar = (dia * 60) + (km * 0.15)
print('O total a pagar é R$ {:.2f}'.format(pagar))
