# Desafio 084
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

principal = list()
temp = list()
totmai = 0
totmen = 0
maior = 0
menor = 0

for c in range(0, 3):
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(principal) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    principal.append(temp[:]) # cópia
    temp.clear()

    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

print(f'Os dados foram {principal}')
print(f'Ao todo, você cadastrou {len(principal)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')

for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')

for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()