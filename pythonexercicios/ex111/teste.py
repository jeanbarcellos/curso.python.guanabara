# Desafio 111
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando..

from ex111.utilidadesCeV import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p)
