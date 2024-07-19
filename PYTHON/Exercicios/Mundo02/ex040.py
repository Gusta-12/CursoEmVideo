# Reprovado, recuperação e aprovado
print('-=-' * 15)
cor = {'limpo' : '\033[m',
       'reprovado' : '\033[1;31m',
       'recuperacao' : '\033[1;33m',
       'aprovado' : '\033[1;32m'}
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Média:', m)
if m < 5.0:
    print('{}ALUNO REPROVADO!{}'.format(cor['reprovado'], cor['limpo']))
elif 5.0 <= m < 7:
    print('{}ALUNO EM RECUPERAÇÃO!{}'.format(cor['recuperacao'], cor['limpo']))
else:
    print('{}ALUNO APROVADO{}'.format(cor['aprovado'], cor['limpo']))
print('-=-' * 15)
