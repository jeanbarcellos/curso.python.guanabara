# Escreva um programa que leia a velocidade de um carro.
# Se aele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ee foi multado
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    print('MULTADO: Você eecedeu o limite permitido que é cd 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma nulta de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
