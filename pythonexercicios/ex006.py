# Um algorítimo que recebe um número e retorna o dobro,
# o triplo e a raiz quadrada do seu valor.

n = int(input('Digite um número qualquer: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1 / 2)  # pow(n, (1/2)

print('O dobro de {} vale {}'.format(n, dobro))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, triplo, n, raiz))
