


x = input('Digite o primeiro número: ')
y = input('Digite o segundo número: ')

escolha = print('''
    Selecione a operação:
        1. Adição
        2. Subtração
        3. Multiplicação
        4. Divisão
      ''')

if escolha == '1':
    print(f'O resultado é: {x + y}')
elif escolha == '2':
    print(f'O resultado é: {x - y}')
elif escolha == '3':
    print(f'O resultado é: {x * y}')
elif escolha == '4':
    print(f'O resultado é: {x / y}')
else:
    print('Erro. Tente novamente.')

