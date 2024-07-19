valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = valores[c]    
    elif valores[c] > maior:
        maior = valores[c]
    elif valores[c] < menor:
        menor = valores[c]
print('-=-' * 15)
print(f'Valores digitados: {valores}')
print(f'Maior valor digitado: {maior} nas posiões: ', end='')
for i, v in enumerate(valores): # da tanto o dado, quanto a posição
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'Menor valor digitado: {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')