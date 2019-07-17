
while True:
    n = int(input('Digite um número para ver a sua tabuada: '))

    print('-' * 30)

    if n < 0:
        break

    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')

    print('-' * 30)

print('Programa tabuada encerrado.')
