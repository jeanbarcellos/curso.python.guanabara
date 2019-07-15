# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calculo o
# comprimento da hipotenusa

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# hi = (co ** 2 + ca ** 2) ** (1/2) # forma matemática
hi = hypot(co, ca)

print('A hipotenuma vai medir {:.2f}'.format(hi))


