# Escreva um prorama que converta uma temperatura digitada em Cº em Fº

c = float(input('Informe a temperatura em Cº: '))
# f = ((9 * c) / 5) + 32
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
