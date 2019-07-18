# Aula 16 - Tuplas

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-' * 70)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')
print('-' * 70)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
print('-' * 70)

print(sorted(lanche))  # ordenado
print('-' * 70)

print(lanche)
print('-' * 70)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))  # quantidade de repeticoes
print(c.index(8))  # posicao do elemento

print('-' * 70)


pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
print(pessoa)