pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-' * 30)

for k in pessoas.keys():
    print(k)

print('-' * 30)

for k in pessoas.values():
    print(k)

print('-' * 30)

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-' * 30)

print(pessoas)
del pessoas['sexo']
print(pessoas)
pessoas['nome'] = 'Leandro'
print(pessoas)