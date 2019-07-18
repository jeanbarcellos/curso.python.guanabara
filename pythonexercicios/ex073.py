# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético-MG',
         'Botafogo', 'Goiás', 'São Paulo', 'Grêmio', 'Bahia', 'Fortaleza',
         'Corinthians', 'Athletico-PR', 'Ceará', 'Vasco', 'Fluminense',
         'Chapecoense', 'Cruzeiro', 'CSA', 'Avaí')

print('-=' * 20)
print(f'Lista de times do brasileião:\n{times}')
print('-=' * 20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print('Posição do chapecoense')
print(f'O Chapecoense está {times.index("Chapecoense") + 1}ª posição')
