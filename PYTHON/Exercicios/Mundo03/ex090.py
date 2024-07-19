aluno = {}
aluno['Nome'] = str(input('Nome: ')).title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('--' * 5)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
print('--' * 5) 