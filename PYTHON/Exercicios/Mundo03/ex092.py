from datetime import date
dados = {}
dados['nome'] = str(input('Nome: ')).capitalize()

nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc

dados['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))

    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year) # Pega quando vai se aposentar, subtrai pelo ano atual, e soma com a idade atual(somando o quanto falta pra se aposentar/ quando se aposentou)

print('-=-' * 15)
for k, v in dados.items():
    print(f' - {k} tem o valor: {v}')
