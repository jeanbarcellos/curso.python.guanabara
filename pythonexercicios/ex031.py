

distancia = float(input('Qual é a distância da sua viagem? '))

print('Você está prestar a começar uma viagem de {}Km'.format(distancia))

'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('E o preço de sua passagem será  de R${:.2f}'.format(preco))