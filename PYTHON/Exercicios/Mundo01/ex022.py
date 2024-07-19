# Manipulando caracteres
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome é {}.'.format(nome))
print('''Com apenas letras maiusculas: {}
Com apenas letras minusculas: {}'''.format(nome.upper(), nome.lower()))
print('Quantas letras tem: {}'.format(len(nome) - nome.count(' ')))
#print('Quantas letras tem o primeiro nome: {}.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, e ele tem {} letras.'.format(separa[0], len(separa[0])))