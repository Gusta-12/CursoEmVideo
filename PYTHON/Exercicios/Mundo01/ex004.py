# .is (Dissecando a variavel)
algo = input('Escreva algo: ')
print('o tipo primitivo desse valor é', type(algo))
print('{} só tem espaços?'.format(algo), algo.isspace())
print('{} é um número?'.format(algo), algo.isnumeric())
print('{} é alfabético?'.format(algo), algo.isalpha())
print('{} possui números/letras?'.format(algo), algo.isalnum())
print('{} está apenas com letras maiúsculas?'.format(algo), algo.isupper())
print('{} está apenas com letras minúsculas?'.format(algo), algo.islower())
print('{} está capitalizada?'.format(algo), algo.istitle())
# Capitalizada = se a primeira letra é maiúscula e o restante pe minúscula. Ex: Gustavo, Brasil, Potato
