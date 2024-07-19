pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '19'}
# for k in pessoas.keys():
#     print(k)
# for v in pessoas.values():
#     print(v)
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
