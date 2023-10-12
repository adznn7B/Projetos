# Biblioteca para criar a função de limpar a tela
import os

# Função para limpar a tela do terminal/console
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que permite ao usuário escolher uma operação matemática
def escolhaOperacao():
    # Apresenta as opções de operações disponíveis
    print('\n0 - Soma')
    print('1 - Subtração')
    print('2 - Multiplicação')
    print('3 - Divisão')
    print('4 - Exponenciação\n')

    # Solicita ao usuário que escolha uma operação
    operacao = int(input('Escolha a operação que deseja realizar: '))

    # Verifica se a escolha do usuário é válida; caso contrário, pede novamente
    while operacao not in [0, 1, 2, 3, 4]:
        limparTela()

        print('\nNão existe nenhuma operação para esse número. Tente novamente!')
        print('\n0 - Soma')
        print('1 - Subtração')
        print('2 - Multiplicação')
        print('3 - Divisão')
        print('4 - Exponenciação\n')

        operacao = int(input('Escolha a operação que deseja realizar: '))
    else:
        return operacao

# Função que permite ao usuário fornecer os valores para a operação
def escolhaValores():
    limparTela()

    # Informa ao usuário qual operação ele escolheu anteriormente
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
    
    # Solicita ao usuário os valores a serem operados
    print('\nQual o primeiro valor?')
    x = float(input('R: '))
    print('\nQual o segundo valor?')
    y = float(input('R: '))

    return x, y

# Função que realiza a operação escolhida e exibe o resultado
def retornoOperacao():
    # Executa a operação matemática com base na escolha do usuário e exibe o resultado
    if operacao == 0:
        z = x + y
        print(f'\n>>> {x} + {y} = {z}')
    elif operacao == 1:
        z = x - y
        print(f'\n>>> {x} - {y} = {z}')
    elif operacao == 2:
        z = x * y
        print(f'\n>>> {x} x {y} = {z}')
    elif operacao == 3:
        z = x / y
        print(f'\n>>> {x} / {y} = {z}')
    else:
        z = x ** y
        print(f'\n>>> {x} ** {y} = {z}')

# Função que verifica se o usuário deseja realizar outra operação
def outraOperacao():
    print("\n=============================")
    print('Deseja realizar outra operação?')
    print('\n0 - Sim')
    print('1 - Não')

    # Solicita ao usuário se ele deseja continuar ou encerrar o programa
    i = int(input('\nR: '))
    while i != 0 and i != 1:
        limparTela()

        print('\nNão existe nenhuma operação para esse número. Tente novamente!')
        print('\n0 - Sim')
        print('1 - Não\n')

        i = int(input('R: '))

    return i

# Inicializa a variável de controle do loop principal
i = 0

# Loop principal do programa
while i == 0:
    limparTela()
    operacao = escolhaOperacao()    # Solicita a operação desejada
    x, y = escolhaValores()         # Solicita os valores a serem operados
    retornoOperacao()               # Realiza a operação e exibe o resultado
    i = outraOperacao()             # Pergunta se o usuário deseja continuar
else:
    limparTela()
    print('Obrigado e volte sempre!') # Mensagem final ao sair do programa