# Reescreva a função leitaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie uma função leiaFloat() com a mesma funcionalidade


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\33[m')
        else:
            break
    return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except:
            print('\033[0;31mERRO! Digite um número real válido.\33[m')
        else:
            break
    return valor


n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')

print(f'O número inteiro digitado foi {n1} e o real foi {n2}')
