# primeiro e ultimo nome
n = str(input('Qual seu nome? ')).strip()
nome = n.split()
print('Seu nome é:', n)
print('Seu primeiro nome é: {} \nSeu último nome é: {}'.format(nome[0], nome[len(nome)-1]))