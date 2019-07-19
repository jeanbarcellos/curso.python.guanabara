# Desafio 081
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()

while True:
    n = int(input('Digite um valor: '))
    valores.append(n)

    r = str(input('Quer continuar? [S/N] '))

    if r in 'Nn':
        break

print('-=' * 30)

print(f'Você digitou {len(valores)} elementos')

valores.sort(reverse=True)
print(f'Os valors em ordem decrecente são: {valores}')

if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor não foi encontrado na lista!')