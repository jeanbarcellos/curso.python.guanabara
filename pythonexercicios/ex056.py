
somaIdade = 0
mediaIdade = 0
m = 2
nomeVelho = ''
maiorIdadeHomem = 0
totMulher20 = 0

for p in range(1, (m +1)):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaIdade += idade

    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade <20:
        totMulher20 += 1

mediaIdade = somaIdade / m

print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem do mais velho tem {} anos se chama {} '.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulher20))
