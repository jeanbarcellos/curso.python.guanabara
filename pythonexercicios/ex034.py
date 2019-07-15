#
# Escreva um programa que pergunte o salário de um cunfionário e calcule o valor do seu aumento.
# Para salários superiores a 1250,00, calculo um aumento de 10%
# par salarios infoeriores ou iguais, o amuro é de 15%

salario = float(input('Qual é o salário do funcionário? '))

if salario <= 1250:
    novo = salario + (salario * 15 /100)
else:
    novo = salario + (salario * 10 /100)

print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(salario, novo))