from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

v = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break;
    elif tipo == 'I':
        if total % 1 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break

    print('=-' * 15)

    print('Vamos jogar novamente... ')
print(f'GAME OVER! Você venceu {v} vezes')

