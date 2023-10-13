import os
import time

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.1)
    
def telaInicio():
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
                portfolio = mostrarPortfolio()
                if portfolio == 0:
                    continue
                else:
                    limparTela()
                    print('Obrigado e volte sempre!')
                    break
            else:
                print('Deu merda')
                break

def mostrarPortfolio():
    limparTela()
    print('\n[0] Chevrolet Tracker - R$120/dia')
    print('[1] Chevrolet Onix - R$90/dia')
    print('[2] Chevrolet Spin - R$150/dia')
    print('[3] Hyundai HB20 - R$85/dia')
    print('[4] Hyundai Tucson - R$120/dia')
    print('[5] Fiat Uno - R$60/dia')
    print('[6] Fiat Mobi - R$70/dia')
    print('[7] Fiat Pulse - R$130/dia')
    print('\n=================================')
    print('\n0 - Continuar')
    print('1 - Sair')
    print('\nO que deseja fazer?')
    portfolio = int(input('R: '))
    while portfolio not in [0, 1]:
        limparTela()
        print(f'\nNão existe nenhum caminho com o número {portfolio}!')
        print('Tente novamente!')
        print('[0] Chevrolet Tracker - R$120/dia')
        print('\n[1] Chevrolet Onix - R$90/dia')
        print('[2] Chevrolet Spin - R$150/dia')
        print('[3] Hyundai HB20 - R$85/dia')
        print('[4] Hyundai Tucson - R$120/dia')
        print('[5] Fiat Uno - R$60/dia')
        print('[6] Fiat Mobi - R$70/dia')
        print('[7] Fiat Pulse - R$130/dia')
        print('\n=================================')
        print('\n0 - Continuar')
        print('1 - Sair')
        print('\nO que deseja fazer?')
        portfolio = int(input('R: '))
    else:
        return portfolio
    
telaInicio()