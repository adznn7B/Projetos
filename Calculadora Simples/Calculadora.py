def escolhaOperacao():
    print('\n0 : Soma')
    print('1 : Subtração')
    print('2 : Multiplicação')
    print('3 : Divisão')
    print('4 : Exponenciação\n')

    operacao = int(input('Escolha a operação que deseja realizar: '))

    return operacao

operacao = escolhaOperacao()