num = [2, 5, 9, 1]
num[2] = int(input('Num: ')) # Altera um valor
num.append(7) # Cria um novo indice com o valor determinado
num.sort(reverse=True) # Ordena os valores, do maior para o menor (reverse)
num.insert(2, 2) # Insere um novo valor, sem exclui-lo
#num.pop() # Elimina o valor desejado (se não for especificado, o primeiro valor será excluido)
num.remove(2) # Remove o primeiro número escolhido
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
