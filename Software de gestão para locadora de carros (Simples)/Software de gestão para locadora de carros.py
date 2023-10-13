import os
import time

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.1)
    
def telaInicio():
    encerrar = False
    carrosDisponiveis = {'Chevrolet Tracker - R$120/dia': 120,
                        'Chevrolet Onix - R$90/dia': 90,
                        'Chevrolet Spin - R$150/dia': 150,
                        'Hyundai HB20 - R$85/dia': 85,
                        'Hyundai Tucson - R$120/dia': 120,
                        'Fiat Uno - R$60/dia': 60,
                        'Fiat Mobi - R$70/dia': 70,
                        'Fiat Pulse - R$130/dia': 130}
    while True:
        limparTela()
        print('\n===============================')
        print('Bem vindo à locadora de carros!')
        print('===============================')
        print('\n0 - Mostrar portfólio')
        print('1 - Alugar um carro')
        print('2 - Devolver um carro')
        print('\nO que deseja fazer?')
        objetivo = int(input('R: '))
        
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
            if objetivo == 0:
                portfolio = mostrarPortfolio(carrosDisponiveis)
                if portfolio == 0:
                    continue
                else:
                    limparTela()
                    print('Obrigado e volte sempre!')
                    break
            elif objetivo == 1:
                encerrar = aluguelCarro(carrosDisponiveis)
                if encerrar:
                    break
            else:
                print('Deu merda')
                break

    return carrosDisponiveis

def mostrarPortfolio(carrosDisponiveis):
    limparTela()
    print("Segue nosso portfólio dos carros disponíveis!\n")
    for indice, carro in enumerate(carrosDisponiveis):
        print(f'[{indice}] {carro}')
    print('\n=================================')
    print('\n0 - Continuar')
    print('1 - Sair')
    print('\nO que deseja fazer?')
    portfolio = int(input('R: '))
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
    
def aluguelCarro(carrosDisponiveis):
    limparTela()
    print("Segue nossos carros disponíveis para aluguel!\n")
    for indice, carro in enumerate(carrosDisponiveis):
        print(f'[{indice}] {carro}')
    print('\n=================================')
    while True:
        try:
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
    diasAluguel = int(input('Escolha por quantos dias deseja alugar: '))
    preco = list(carrosDisponiveis.values())[carroEscolhido]
    limparTela()
    nomeCarro = list(carrosDisponiveis.keys())[carroEscolhido]
    print(f'\nVocê escolheu {nomeCarro} por {diasAluguel} dias.')
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
            print(f'\nParabéns você escolheu {nomeCarro} por {diasAluguel} dias.')
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

carrosDisponiveis = telaInicio()