# Desafio 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)


def notas(*n, sit=False):
    """
    -> Função para analizar as notas e situações de vários alunos
    :param n: Uma ou mais notas dos alunos (aceita vários)
    :param sit: (Opcional) Indica se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'

    return r


resp = notas(5.5, 2.5, 8.5)
print(resp)
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)

help(notas)
