# IMC
print('-=-' * 15)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2
print('IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('Classificação: ABAIXO DO PESO.')
elif imc <= 25:
    print('Classificação: PESO IDEAL.')
elif imc <= 30:
    print('Classificação: SOBREPESO.')
elif imc <= 40:
    print('Classificação: OBESIDADE.')
else:
    print('Classificação: OBESIDADE MÓRBIDA.')
print('-=-' * 15)