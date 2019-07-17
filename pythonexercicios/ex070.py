total = 0
totMil = 0
menor = 0
cont = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1

    if preco > 1000:
        totMil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in ('SN'):
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totMil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')
