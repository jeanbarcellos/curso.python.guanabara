# Leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

soma = 0
cont = 0

for c in range(0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Você informou {} nmúmeros PARES e a soma foi {}'.format(cont, soma))