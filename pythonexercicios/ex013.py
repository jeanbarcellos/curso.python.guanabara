# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário com 15% de aumento

salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganha R${:.2f}, com 15% de aumento, passará a receber R$ {:.2f}'.format(salario, novo))