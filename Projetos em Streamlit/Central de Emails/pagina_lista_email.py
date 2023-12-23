# Importação das bibliotecas necessárias
import streamlit as st
from utilidades import *

# Função para exibir a página de gerenciamento da lista de emails
def pag_lista_email():
    # Cria um cabeçalho na página
    st.markdown('# Lista de Emails')
    st.divider()

    # Itera sobre todos os arquivos de texto na pasta de listas de email
    for arquivo in pasta_lista.glob('*.txt'):
        # Formata o nome do arquivo para exibição
        nome_arquivo = arquivo.stem.replace('_', ' ').upper()

        # Cria colunas para botões de ação para cada lista de email
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(nome_arquivo, key=f'{nome_arquivo}', use_container_width=True, on_click=_usa_lista, args=(nome_arquivo, ))
        col2.button('Editar', key=f'editar_{nome_arquivo}', use_container_width=True, on_click=editar_lista, args=(nome_arquivo, ))
        col3.button('Remover', key=f'remover_{nome_arquivo}', use_container_width=True, on_click=remove_lista, args=(nome_arquivo, ))
    
    st.divider()
    # Botão para adicionar uma nova lista de emails
    st.button('Adicionar Lista', on_click=mudar_pagina, args=('adicionar_nova_lista',))
    
# Função para adicionar uma nova lista de emails
def pag_adicionar_nova_lista(nome_lista='', emails_lista=''):
    # Campo de entrada para o nome da lista
    nome_lista = st.text_input('Nome da lista: ', value=nome_lista)
    # Área de texto para inserir os emails, separados por vírgula
    emails_lista = st.text_area('Escreva os emails separados por vírgula: ', value=emails_lista, height=600)
    # Botão para salvar a nova lista
    st.button('Salvar', on_click=salvar_lista, args=(nome_lista, emails_lista))

# Função para usar uma lista de emails existente
def _usa_lista(nome):
    # Lê o arquivo da lista de emails e atualiza a sessão do Streamlit com esses emails
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_lista / nome_arquivo) as f:
        texto_arquivo = f.read()
    st.session_state.destinatarios_atual = texto_arquivo
    mudar_pagina('home')
       
# Função para salvar uma nova lista de emails
def salvar_lista(nome, texto):
    # Garante a existência da pasta de listas e salva o arquivo da nova lista
    pasta_lista.mkdir(exist_ok=True)
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_lista / nome_arquivo, 'w') as f:
        f.write(texto)
    mudar_pagina('lista_emails')
    
# Função para remover uma lista de emails existente
def remove_lista(nome):
    # Remove o arquivo da lista de emails
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    (pasta_lista / nome_arquivo).unlink()

# Função para editar uma lista de emails existente
def editar_lista(nome):
    # Lê o arquivo da lista de emails para edição
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_lista / nome_arquivo) as f:
        texto_arquivo = f.read()
    # Atualiza a sessão do Streamlit com os dados da lista a ser editada
    st.session_state.nome_lista_editar = nome
    st.session_state.texto_lista_editar = texto_arquivo
    mudar_pagina('editar_lista')