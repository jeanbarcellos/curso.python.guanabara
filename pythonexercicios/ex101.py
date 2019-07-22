# Desafio 101
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date  # escopo de importacao
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 < idade < 18 or idade > 65:
        return f'Com {idade} anos: NÃO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print(voto(1940))
print(voto(1990))
print(voto(2000))
print(voto(2010))
