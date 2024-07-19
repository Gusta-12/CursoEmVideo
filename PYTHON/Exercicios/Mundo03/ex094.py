galera = []
pessoa = {}
midade = idade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()

    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F...')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    
    pessoa['idade'] = int(input('Idade: '))
    idade += pessoa['idade']

    galera.append(pessoa.copy())
    pessoa.clear()

    opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while opc not in 'SN':
        print('ERRO! Responda apenas S ou N')
        opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if opc == 'N':
        break

print('-=-' * 15)
print(f'A) O grupo tem {len(galera)} pessoas cadastradas.')
print()
midade = idade / len(galera)
print(f'B) A média de idade é de {midade:.2f} anos.')
print()
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end='; ')
print()
print()
print('D) Pessoas acima da média:')
for c in galera:
    if c['idade'] > midade:
        for i, v in c.items():
            print(f' {i} = {v};', end='')
        print()
print()
print('<< ENCERRANDO >>')
