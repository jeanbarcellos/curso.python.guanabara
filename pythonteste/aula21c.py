"""
def teste():
    x = 8  # variável local
    print(f'Na função, n vale {n}')
    print(f'Na função, x vale {x}')


n = 2  # variável global
print(f'No programa principal, n vale {n}')
teste()
"""


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
