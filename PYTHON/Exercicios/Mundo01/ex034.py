# Aumento
sal = float(input('Digite o salário do(a) funcionário(a): '))
if sal > 1250.00:
    nov = sal + (sal * 10 / 100)
else:
    nov = sal + (sal * 15 / 100)
print('O novo salário do(a) funcionário(a) será de R$ {:.2f}'.format(nov))
