# RETORNO


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


resp = somar(3, 2, 5)
print(f'A soma vale {resp}')
print(somar(2, 2))
print(somar(6))

print('-' * 50)


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1} {f2} {f3}')

print('-' * 50)


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('É impar')
