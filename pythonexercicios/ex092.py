# Desafio 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()
dados['nome'] = str(input(f'Nome: '))

nasc = int(input(f'Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc

dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['conratacao'] = int(input('Ano de Contraração: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoris'] = dados['idade'] + ((dados['conratacao'] + 35) - datetime.now().year)

print(dados)
for k, v in dados.items():
    print(f'  = {k} tem valor {v}')
