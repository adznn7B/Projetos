# Importação de módulos necessários
import streamlit as st
from utilidades import *

# Função para exibir a página de configurações
def pag_configuracao():
    # Cria um cabeçalho na página
    st.markdown('# Configuração')
    
    # Cria um campo de input para o email do usuário
    email = st.text_input('Digite o seu email:')
    
    # Cria um botão para salvar o email
    st.button('Salvar', key='salvar_email', on_click=_salvar_email, args=(email, ))
    
    # Cria um campo de input para a chave do Gmail
    chave = st.text_input('Digite a chave Gmail:')
    
    # Cria um botão para salvar a chave
    st.button('Salvar', key='salvar_chave', on_click=_salvar_chave, args=(chave, ))
    
# Função para salvar o email do usuário
def _salvar_email(email):
    # Garante a existência da pasta de configurações
    pasta_configuracoes.mkdir(exist_ok=True)
    
    # Salva o email do usuário em um arquivo
    with open(pasta_configuracoes / 'email_usuario.txt', 'w') as f:
        f.write(email)

# Função para salvar a chave do Gmail do usuário
def _salvar_chave(chave):
    # Garante a existência da pasta de configurações
    pasta_configuracoes.mkdir(exist_ok=True)
    
    # Salva a chave do Gmail do usuário em um arquivo
    with open(pasta_configuracoes / 'chave.txt', 'w') as f:
        f.write(chave)

# Função para ler o email do usuário da configuração
def _le_email_usuario():
    # Garante a existência da pasta de configurações
    pasta_configuracoes.mkdir(exist_ok=True)
    
    # Verifica se o arquivo com o email do usuário existe e lê seu conteúdo
    if (pasta_configuracoes / 'email_usuario.txt').exists():
        with open(pasta_configuracoes / 'email_usuario.txt', 'r') as f:
            return f.read()
    return ''

# Função para ler a chave do Gmail do usuário da configuração
def _le_chave_usuario():
    # Garante a existência da pasta de configurações
    pasta_configuracoes.mkdir(exist_ok=True)
    
    # Verifica se o arquivo com a chave do Gmail existe e lê seu conteúdo
    if (pasta_configuracoes / 'chave.txt').exists():
        with open(pasta_configuracoes / 'chave.txt', 'r') as f:
            return f.read()
    return ''