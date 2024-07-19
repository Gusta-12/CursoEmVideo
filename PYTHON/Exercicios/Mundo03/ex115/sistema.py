from pac.interface import * # importa tudo
from pac.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resp = menu(['Listar Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resp == 1:
        # Listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # Cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema...')
        sleep(1)
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
        sleep(1)
    sleep(1)