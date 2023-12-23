# Importa a biblioteca necessária para o simulador
import random
import os
import time

class Academia:
    def __init__(self):
        # Inicializa uma lista de halteres pares de 10 a 34.
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        # Atribui cada haltere ao seu respectivo espaço no porta-halteres.
        self.porta_halteres = {i:i for i in self.halteres}

    def listar_halteres(self):
        # Retorna uma lista de halteres que não estão em seus espaços originais.
        return [i for i in self.porta_halteres.values() if i != 0]

    def listar_espacos(self):
        # Retorna uma lista de espaços vazios no porta-halteres.
        return [i for i, j in self.porta_halteres.items() if j == 0]
    
    def pegar_haltere(self, peso):
        # Remove o haltere do porta-halteres.
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso
    
    def devolver_halter(self, pos, peso):
        # Devolve o haltere para um determinado espaço no porta-halteres.
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        # Calcula a proporção de halteres que não estão em seus espaços originais.
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)

class Usuario:
    def __init__(self, tipo, academia):
        # O tipo 1 devolve os halteres corretamente, enquanto o tipo 2 devolve aleatoriamente.
        self.tipo = tipo
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        # O usuário pega um haltere aleatório.
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        # O usuário devolve o haltere.
        espacos = self.academia.listar_espacos()

        # Usuário do tipo 1 tenta devolver o haltere ao espaço correto.
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
        
        # Usuário do tipo 2 sempre devolve o haltere a um espaço aleatório.
        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)
        self.peso = 0
        
# Função para limpar a tela do terminal
def limparTela():
    # Verifica o sistema operacional. Se for Windows (nt) limpa com 'cls', senão limpa com 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
    # Aguarda 0,1 segundos (100 milissegundos)
    time.sleep(0.1)

# Inicializa a academia.
academia = Academia()

# Cria 10 usuários do tipo 1 e 1 usuário do tipo 2.
usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
random.shuffle(usuarios)

# Simula o processo de treino 10 vezes.
for i in range(10):
    random.shuffle(usuarios)
    for user in usuarios:
        user.iniciar_treino()
    for user in usuarios:
        user.finalizar_treino()
        
# Imprime o estado atual do porta-halteres e o nível de "caos".
limparTela()
print("\nEstado do porta-halteres:", academia.porta_halteres)
print(f'\nNível de caos: {round((academia.calcular_caos()*100), ndigits=2)}%')