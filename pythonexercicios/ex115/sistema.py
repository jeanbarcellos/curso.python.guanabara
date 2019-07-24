from time import sleep

while True:
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 40)

    opcao = int(input('\033[1;33mSua opção: \033[m'))

    if opcao == 1:
        print('-' * 40)
        print(f'{"PESSOAS CADASTRADAS":^40}')
        print('-' * 40)
        print('Lista de pessoas.....')
        print('')
        print('-' * 40)

        sleep(2)

    elif opcao == 2:
        print('-' * 40)
        print(f'{"NOVO CADASTRO":^40}')
        print('-' * 40)

        nome = str(input('Nome: '))
        idade = int(input('Idade: '))

        print(f'Registro de {nome} adicionado.')

        sleep(2)
    elif opcao == 3:
        print('-' * 40)
        print(f'{"Saindo do ssitema... Até logo!":^40}')
        print('-' * 40)
        break
    else:
        print('\033[1;31mErro: Digite uma opção válida!\033[m')
        sleep(2)
