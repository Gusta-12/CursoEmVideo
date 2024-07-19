from time import sleep

c = ('\033[m',       # 0 - SEM CORES
     '\033[1;31m',   # 1 - VERMELHO
     '\033[1;32m',   # 2 - VERDE
     '\033[1;34m'    # 3 - AZUL
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)

while True:
    titulo('SISTEMA DE AJUDA PyHelp', 3)
    comando = str(input('Função ou Biblioteca: ')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)