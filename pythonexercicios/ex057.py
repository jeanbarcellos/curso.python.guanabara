
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in ('MF'):
    sexo = str(input('Dados inválidos.\nInforme seu sexo: [M/F] ')).strip().upper()[0]

print('Sexo {} registrado com sucesso.'.format(sexo))