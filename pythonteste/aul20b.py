def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(4, 5)
soma(a=4, b=5)
soma(b=4, a=5)

print('-' * 40)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos  {s}')


soma(5, 2)
soma(2, 9, 4)
