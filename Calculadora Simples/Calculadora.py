import os

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def escolhaOperacao():
    print('\n0 : Soma')
    print('1 : Subtração')
    print('2 : Multiplicação')
    print('3 : Divisão')
    print('4 : Exponenciação\n')

    operacao = int(input('Escolha a operação que deseja realizar: '))

    if operacao != 0 and operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
        raise print('Não existe nenhuma operação para esse número. Tente novamente!')
    else:
        return operacao

def escolhaValores():
    limparTela()

    if operacao == 0:
        print('A operação escolhida foi a de soma!')
    elif operacao == 1:
        print('A operação escolhida foi a de subtração!')
    elif operacao == 2:
        print('A operação escolhida foi a de multiplicação!')
    elif operacao == 3:
        print('A operação escolhida foi a de divisão!')
    else:
        print('A operação escolhida foi a de exponenciação!')
    
    print('\nQual o primeiro valor?')
    x = float(input('R: '))

    print('\nQual o segundo valor?')
    y = float(input('R: '))

    return x, y

operacao = escolhaOperacao()
x, y = escolhaValores()