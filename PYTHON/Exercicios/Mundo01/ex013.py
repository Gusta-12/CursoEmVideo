# Salário
nome = input('Qual o nome do(a) funcionário(a)? ')
sal = float(input('Qual o salário do(a) funcionário(a)? R$ '))
aumento = sal + (sal * 15/100)
print('O novo salário do(a) {} será de R$ {:.2f}.'.format(nome, aumento))
