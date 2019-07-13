# nome = input('Qual o seu nome? ')
#
# # adicionando espaços
# print('Prazer em te conhecer {:20}!'.format(nome))
#
# # com alinhamento a direita
# print('Prazer em te conhecer {:>20}!'.format(nome))
#
# # com alinhamento a esquerda
# print('Prazer em te conhecer {:<20}!'.format(nome))
#
# # com alinhamento centralizado
# print('Prazer em te conhecer {:^20}!'.format(nome))
#
# print('Prazer em te conhecer {:=^20}!'.format(nome))

# print('Seu nome é {:=^20}'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma de {} e {} é {}'.format(n1, n2, s))
print('A subtração é {}'.format(sb))
print('A multiplicação é {}'.format(m))
print('A divisão é {:.2f}'.format(d))  # arredondando o resultado para 2 casas decimais
print('A divisão inteira é {}'.format(di))
print('A potência é {}'.format(e))

print('Linha 1', end=' ')
print('Linha 2 sem quebra')
