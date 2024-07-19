try:
    a = int(input('Numerador/Dividendo: '))
    b = int(input('Denominador/Divisor: '))
    r = a / b
except (ValueError, TypeError):
    print('Houve um problema com o tipo dos dados informados.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt: # ctrl + C
    print('Não houve nenhum dado informado!')
else:
    print(f'O resultado de {a} / {b} é {r:.1f}')
finally:
    print('Volte sempre!')