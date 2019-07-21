# enpacotamento
# variaveis diversoas


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)

print('-' * 40)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos  {s}')


soma(5, 2)
soma(2, 9, 4)
