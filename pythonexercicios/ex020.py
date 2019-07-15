# O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteado.

import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

list = [n1, n2, n3, n4]
random.shuffle(list)

print('A ordem de apresentação será: ')
print(list)
