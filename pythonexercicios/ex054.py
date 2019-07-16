
from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        #print('Essa pessoa é maior')
    else:
        totmenor += 1
        #print('Essa pessoa é menor')

    #print('Essa pessoa tem {} anos'.format(idade))

print('Total de {} pesssoas maiores de idade'.format(totmaior))
print('Total de {} pesssoas menores de idade'.format(totmenor))