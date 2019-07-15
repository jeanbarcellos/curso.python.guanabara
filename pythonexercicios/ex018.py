# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste angulo

from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo que você deseja: "))

seno = sin(radians(angulo))
cossseno = cos(radians(angulo))
tangenente = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cossseno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangenente))
