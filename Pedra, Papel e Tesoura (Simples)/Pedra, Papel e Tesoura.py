# Importando as bibliotecas necessárias
import os
import time
import random

# Função para limpar a tela do terminal
def limparTela():
    # Verifica o sistema operacional. Se for Windows (nt) limpa com 'cls', senão limpa com 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
    # Aguarda 0,1 segundos (100 milissegundos)
    time.sleep(0.1)

# Função principal do jogo
def jogo(rodadasGanhasUsuario, rodadasGanhasComputador):
    # Lista com as opções de jogadas possíveis
    jogadasPossiveis = ['Pedra', 'Papel', 'Tesoura']
    # Escolha aleatória da jogada do computador
    jogadasComputador = random.randint(0, 2)

    # Solicita ao usuário para escolher uma opção
    print('\nEscolha seu lance:')
    print('0 - Pedra\n1 - Papel\n2 - Tesoura')
    jogadasUsuario = int(input('\nDigite aqui sua jogada: '))

    # Enquanto o usuário não escolher uma opção válida, continua solicitando
    while jogadasUsuario not in [0, 1, 2]:
        limparTela()
        print(f'\nNão existe nenhum lance com o número {jogadasUsuario}.')
        print('Tente novamente!')
        print('\n0 - Pedra\n1 - Papel\n2 - Tesoura')
        jogadasUsuario = int(input('\nDigite aqui sua jogada: '))

    limparTela()

    # Transforma a escolha do usuário e do computador em palavras (Pedra, Papel ou Tesoura)
    resultadoUsuario = jogadasPossiveis[jogadasUsuario]
    resultadoComputador = jogadasPossiveis[jogadasComputador]

    # Mostra as jogadas escolhidas
    print('===========================')
    print(f'Sua jogada: {jogadasPossiveis[jogadasUsuario]}')
    print(f'Jogada do computador: {jogadasPossiveis[jogadasComputador]}')

    # Determina o vencedor da rodada
    if resultadoUsuario == resultadoComputador:
        print('Empate!')
    # Verifica todas as combinações em que o usuário vence
    elif (resultadoUsuario == 'Pedra' and resultadoComputador == 'Tesoura') or \
         (resultadoUsuario == 'Tesoura' and resultadoComputador == 'Papel') or \
         (resultadoUsuario == 'Papel' and resultadoComputador == 'Pedra'):
        rodadasGanhasUsuario += 1
        print('Você venceu!')
    # Caso contrário, o computador vence
    else:
        rodadasGanhasComputador += 1
        print('Você perdeu!')

    # Pergunta se o usuário deseja jogar novamente
    print('\nJogar novamente?')
    print('0 - Sim\n1 - Não')
    continuacao = int(input('\nDigite aqui sua resposta: '))

    # Enquanto o usuário não escolher uma opção válida, continua solicitando
    while continuacao not in [0, 1]:
        limparTela()
        print(f'\nNão existe nenhum caminho com o número {continuacao}')
        print('Tente novamente!')
        print('\nJogar novamente?')
        print('0 - Sim\n1 - Não')
        continuacao = int(input('\nDigite aqui sua resposta: '))

    # Retorna a decisão do usuário e as pontuações atualizadas
    return continuacao, rodadasGanhasUsuario, rodadasGanhasComputador

# Função de início do jogo
def telaInicio():
    rodadasGanhasUsuario = 0
    rodadasGanhasComputador = 0

    # Enquanto o usuário desejar continuar jogando, continua no loop
    continuar = 0
    while continuar == 0:
        limparTela()
        # Mostra mensagem de boas-vindas
        print('\n=============================================')
        print('Bem vindo ao jogo de Pedra, Papel ou Tesoura!')
        print('=============================================')
        # Mostra o placar atual
        print('\nPLACAR:')
        print(f'Você: {rodadasGanhasUsuario}')
        print(f'Computador: {rodadasGanhasComputador}')
        # Chama a função jogo e atualiza as variáveis
        continuar, rodadasGanhasUsuario, rodadasGanhasComputador = jogo(rodadasGanhasUsuario, rodadasGanhasComputador)

    # Quando o usuário decidir não continuar, mostra mensagem de despedida
    limparTela()
    print('Obrigado e volte sempre!')

# Inicia o jogo
telaInicio()