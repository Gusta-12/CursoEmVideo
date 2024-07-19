def contador(* num):
    print(num)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


print('-=-' * 15)
contador(2, 1, 7)
contador(8, 0)
print('-=-' * 15)
soma(2, 1, 7)
soma(8, 0)
print('-=-' * 15)