num = [2, 5, 9, 1]
num[2] = 3
print(num)

num.append(7)  # adiciona

print(num)

num.sort()  # ordena asc
print(num)

num.sort(reverse=True)  #ordena desc
print(num)

print(f'Essa lista tem {len(num)} elementos.')

num.insert(2, 2)  # inserir na posição 2, inserir 0
print(num)

num.remove(2)  # Remove apenas a primeira ocorrencia
print(num)

# num.remove(4) # se não existir, dá erro

