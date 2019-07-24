try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('ERRO! Tipos de dados digitados incorretos!')
except ZeroDivisionError:
    print('ERRO! Não é possível dividir por zero!')
except KeyboardInterrupt:
    print('ERRO! O usuário não informou os dados!')
except Exception as erro:
    print(f'ERRO! Erro genérico. Causa: {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('FIM')
