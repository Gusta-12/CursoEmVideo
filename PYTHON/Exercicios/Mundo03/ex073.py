times = ('Corinthians', 'Palmeiras', 'Santos', 
         'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=-' * 15)
print('Lista de times do Brasileirão:', times)
print('-=-' * 15)
print('Os cinco primeiros são:', times[:5])
print('-=-' * 15)
print('Os quatro ultimos são:', times[-4:])
print('-=-' * 15)
print('Em ordem alfabética:', sorted(times))
print('-=-' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print('-=-' * 15)