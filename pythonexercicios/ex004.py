#  Um programa que recebe qualquer coisa, retornando o seu
#  tipo primitivo e todas informações sobre o dado recebido.

e = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(e)}')

print('Só tem espaços? {}'.format(e.isspace()))
print('É um número? {}'.format(e.isnumeric()))
print('É alfabético ? {}'.format(e.isalpha()))
print('É alfanumérico? {}'.format(e.isalnum()))
print('Está em minúsculo? {}'.format(e.islower()))
print('Está em maiúsculo? {}'.format(e.isupper()))