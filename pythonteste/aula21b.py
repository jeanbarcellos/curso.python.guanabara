# PARAMETROS OPCIONAIS


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: Prinmeiro Valor
    :param b: Segundo Valor
    :param c: Terceiro Valor
    :return: sem retorno
    Autor: Gustavo Guanabara
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(2)
somar()
