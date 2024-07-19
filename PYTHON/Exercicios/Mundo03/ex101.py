def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos, o voto é: OBRIGATÓRIO!'
    elif idade >= 16 or idade >= 65:
        return f'Com {idade} anos, o voto é: OPCIONAL!'
    else:
        return f'Com {idade} anos, o voto é: NEGADO!'
    

print('--' * 20)
nasc = int(float(input('Digite o ano em que você nasceu: ')))
print(voto(nasc))