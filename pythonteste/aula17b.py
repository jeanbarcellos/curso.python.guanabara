a = [2, 3, 4, 7]

# b = a  # As liastas fazem referenca
b = a[:]  # Cria uma copia de a

b[2] = 8

print(f'Lista a {a}')
print(f'Lista b {b}')

