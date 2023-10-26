# Importa os módulos necessários.
import os
import time

# Dicionário global para armazenar os carros que foram alugados.
carrosAlugados = {}

# Função para limpar a tela.
def limparTela():
    # Limpa a tela dependendo do sistema operacional.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Aguarda um curto período de tempo após limpar a tela.
    time.sleep(0.1)
    
# Função que exibe a tela inicial do programa.
def telaInicio():
    # Flag para determinar se o programa deve ser encerrado.
    encerrar = False

    # Dicionário com os carros disponíveis e seus respectivos preços por dia.
    carrosDisponiveis = {'Chevrolet Tracker - R$120/dia': 120,
                        'Chevrolet Onix - R$90/dia': 90,
                        'Chevrolet Spin - R$150/dia': 150,
                        'Hyundai HB20 - R$85/dia': 85,
                        'Hyundai Tucson - R$120/dia': 120,
                        'Fiat Uno - R$60/dia': 60,
                        'Fiat Mobi - R$70/dia': 70,
                        'Fiat Pulse - R$130/dia': 130}
    
    # Loop infinito para manter a tela inicial aberta.
    while True:
        # Limpa a tela e exibe as opções.
        limparTela()
        print('\n===============================')
        print('Bem vindo à locadora de carros!')
        print('===============================')
        print('\n0 - Mostrar portfólio')
        print('1 - Alugar um carro')
        print('2 - Devolver um carro')
        print('\nO que deseja fazer?')

        # Solicita ao usuário a opção desejada.
        objetivo = int(input('R: '))
        
        # Verifica se a opção escolhida é válida.
        while objetivo not in [0, 1, 2]:
            limparTela()
            print(f'Não existe nenhum caminho com o número {objetivo}!')
            print('Tente novamente!')
            print('\n0 - Mostrar portfólio')
            print('1 - Alugar um carro')
            print('2 - Devolver um carro')
            print('\nO que deseja fazer?')
            objetivo = int(input('R: '))
        else:
            # Se a opção for 0, mostra o portfólio.
            if objetivo == 0:
                portfolio = mostrarPortfolio(carrosDisponiveis)
                # Se a opção for continuar, volta para a tela inicial.
                if portfolio == 0:
                    continue
                else:
                    # Caso contrário, encerra o programa.
                    limparTela()
                    print('Obrigado e volte sempre!')
                    break
            # Se a opção for 1, inicia o processo de aluguel de carro.
            elif objetivo == 1:
                encerrar = aluguelCarro(carrosDisponiveis)
                # Se a flag encerrar for True, encerra o programa.
                if encerrar:
                    break
            # Se a opção for 2, inicia o processo de devolução de carro.
            elif objetivo == 2:
                devolverCarro(carrosDisponiveis)
            else:
                # Caso a opção não seja nenhuma das anteriores (isso não deveria acontecer).
                print('Opção não implementada.')
                break
    return carrosDisponiveis

# Função que exibe o portfólio de carros disponíveis.
def mostrarPortfolio(carrosDisponiveis):
    limparTela()
    print("Segue nosso portfólio dos carros disponíveis!\n")
    for indice, carro in enumerate(carrosDisponiveis):
        print(f'[{indice}] {carro}')
    print('\n=================================')
    print('\n0 - Continuar')
    print('1 - Sair')
    print('\nO que deseja fazer?')

    # Solicita ao usuário a opção desejada.
    portfolio = int(input('R: '))

    # Verifica se a opção escolhida é válida.
    while portfolio not in [0, 1]:
        limparTela()
        print(f'\nNão existe nenhum caminho com o número {portfolio}!')
        print('Tente novamente!\n')
        for indice, carro in enumerate(carrosDisponiveis):
            print(f'[{indice}] {carro}')
        print('\n=================================')
        print('\n0 - Continuar')
        print('1 - Sair')
        print('\nO que deseja fazer?')
        portfolio = int(input('R: '))
    else:
        return portfolio

# Função para o processo de aluguel de carros. 
def aluguelCarro(carrosDisponiveis):
    limparTela()
    print("Segue nossos carros disponíveis para aluguel!\n")
    for indice, carro in enumerate(carrosDisponiveis):
        print(f'[{indice}] {carro}')
    print('\n=================================')
    while True:
        try:
            # Solicita ao usuário o carro desejado e valida a entrada.
            carroEscolhido = int(input('\nEscolha o código do carro: '))
            if 0 <= carroEscolhido < len(carrosDisponiveis):
                break
            else:
                limparTela()
                print("Por favor, escolha um código de carro válido.\n")
                for indice, carro in enumerate(carrosDisponiveis):
                    print(f'[{indice}] {carro}')
        except ValueError:
            print("Por favor, insira um número.")

    # Solicita ao usuário a quantidade de dias de aluguel.
    diasAluguel = int(input('Escolha por quantos dias deseja alugar: '))

    # Calcula o preço total do aluguel.
    preco = list(carrosDisponiveis.values())[carroEscolhido]

    limparTela()
    nomeCarro = list(carrosDisponiveis.keys())[carroEscolhido]
    nomeCarroEscolhido = nomeCarro.split('-')[0].strip()
    print(f'\nVocê escolheu {nomeCarroEscolhido} por {diasAluguel} dias.')
    print(f'O aluguel totalizara R${preco * diasAluguel}. Deseja alugar?')
    print('\n=================================')
    print('\n0 - Sim')
    print('1 - Não')
    respostaAluguel = int(input('\nR: '))
    print('\n=================================')
    while respostaAluguel not in [0, 1]:
        limparTela()
        print(f'Não existe nenhuma opção com o número {respostaAluguel}.')
        print('Tente novamente!')
        print(f'\nO aluguel totalizara R${preco * diasAluguel}. Deseja alugar?')
        print('0 - Sim')
        print('1 - Não')
        respostaAluguel = int(input('\nR: '))
    else:
        if respostaAluguel == 0:
            carrosAlugados[nomeCarro] = carrosDisponiveis.pop(nomeCarro)
            print(f'\nParabéns você escolheu {nomeCarroEscolhido} por {diasAluguel} dias.')
            print('0 - Continuar')
            print('1 - Sair')
            aluguel = int(input('\nR: '))
            while aluguel not in [0, 1]:
                limparTela()
                print(f'Não existe nenhum caminho com o número {aluguel}')
                print('Tente novamente!')
                print('0 - Continuar')
                print('1 - Sair')
                aluguel = int(input('\nR: '))
            else:
                if aluguel == 0:
                    return False
                else:
                    print('\nObrigado e volte sempre!')
                    return True
        else:
            return False
    # Se o usuário confirmar o aluguel, o carro é removido da lista de disponíveis e adicionado na lista de alugados.
    # Caso contrário, retorna para a tela inicial.

# Função para o processo de devolução de carros.
def devolverCarro(carrosDisponiveis):
    limparTela()
    if not carrosAlugados:
        print('Não há carros alugados no momento.')
        time.sleep(2)
        return
    print("Segue a lista dos carros alugados:\n")
    for indice, carro in enumerate(carrosAlugados):
        nomeCarro = carro.split('-')[0].strip()
        print(f'[{indice}] {nomeCarro}')
    print('\n=================================')

    while True:
        try:
            # Solicita ao usuário o carro que deseja devolver e valida a entrada.
            carroEscolhido = int(input('\nEscolha o código do carro que deseja devolver: '))
            if 0 <= carroEscolhido < len(carrosAlugados):
                break
            else:
                limparTela()
                print("Por favor, escolha um código de carro válido.\n")
                for indice, carro in enumerate(carrosAlugados):
                    nomeCarro = carro.split('-')[0].strip()
                    print(f'[{indice}] {nomeCarro}')
        except ValueError:
            print("Por favor, insira um número.")
            
    # O carro é removido da lista de alugados e adicionado de volta na lista de disponíveis.
    nomeCarro = list(carrosAlugados.keys())[carroEscolhido]
    carrosDisponiveis[nomeCarro] = carrosAlugados[nomeCarro]
    del carrosAlugados[nomeCarro]

    # Informa ao usuário que a devolução foi bem-sucedida.
    nomeCarroDevolvido = nomeCarro.split('-')[0].strip()
    print(f'\nVocê devolveu o {nomeCarroDevolvido} com sucesso!')
    time.sleep(2)

# Inicia o programa.
carrosDisponiveis = telaInicio()