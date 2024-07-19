# Palindromo (palavra = de trás pra frente)
print('-=-' * 15)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('\033[1;32mTemos um palíndromo!\033[m')
else:
    print('\033[1;31mNão temos um palíndromo!\033[m')
print('-=-' * 15)