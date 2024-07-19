# Letra 'A'
algo = str(input('Digite algo: ')).upper().strip()
print('A letra \'A\' aparece {} vezes.'.format(algo.count('A')))
print('A primeira letra \'A\' apareceu na posição: {}.'.format(algo.find('A')+1))
print('E pareceu na posição: {} pela última vez.'.format(algo.rfind('A')+1))