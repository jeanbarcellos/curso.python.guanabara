# Escreva um programa que faça o computador "pensar" em um número inteirao entre 0 a 5 e peça para que o
# usuário tentar descobrir qual foi o número escolhido pelo computador. O programador deverá escrever na tela se o
# usuário venceu ou perderu.

from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar ...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')

sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

