# Importação das bibliotecas necessárias
import streamlit as st
from utilidades import *

# Função para exibir a página de gerenciamento de templates
def pag_templates():
    # Cria um cabeçalho na página
    st.markdown('# Templates')
    st.divider()

    # Itera sobre todos os arquivos de texto na pasta de templates
    for arquivo in pasta_templates.glob('*.txt'):
        # Formata o nome do arquivo para exibição
        nome_arquivo = arquivo.stem.replace('_', ' ').upper()

        # Cria colunas para botões de ação para cada template
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(nome_arquivo, key=f'{nome_arquivo}', use_container_width=True, on_click=_usar_template, args=(nome_arquivo, ))
        col2.button('Editar', key=f'editar_{nome_arquivo}', use_container_width=True, on_click=editar_arquivo, args=(nome_arquivo, ))
        col3.button('Remover', key=f'remover_{nome_arquivo}', use_container_width=True, on_click=remove_template, args=(nome_arquivo, ))
    
    st.divider()
    # Botão para adicionar um novo template
    st.button('Adicionar Template', on_click=mudar_pagina, args=('adicionar_novo_template',))
    
# Função para adicionar um novo template
def pag_adicionar_novo_template(nome_template='', texto_template=''):
    # Campo de entrada para o nome do template
    nome_template = st.text_input('Nome do template: ', value=nome_template)
    # Área de texto para inserir o conteúdo do template
    texto_template = st.text_area('Escreva o texto do template: ', value=texto_template, height=600)
    # Botão para salvar o novo template
    st.button('Salvar', on_click=salvar_template, args=(nome_template, texto_template))

# Função para usar um template existente
def _usar_template(nome):
    # Lê o arquivo do template e atualiza a sessão do Streamlit com esse conteúdo
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_templates / nome_arquivo) as f:
        texto_arquivo = f.read()
    st.session_state.corpo_atual = texto_arquivo
    mudar_pagina('home')
    
# Função para salvar um novo template
def salvar_template(nome, texto):
    # Garante a existência da pasta de templates e salva o arquivo do novo template
    pasta_templates.mkdir(exist_ok=True)
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_templates / nome_arquivo, 'w') as f:
        f.write(texto)
    mudar_pagina('templates')
    
# Função para remover um template existente
def remove_template(nome):
    # Remove o arquivo do template
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    (pasta_templates / nome_arquivo).unlink()

# Função para editar um template existente
def editar_arquivo(nome):
    # Lê o arquivo do template para edição
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_templates / nome_arquivo) as f:
        texto_arquivo = f.read()
    # Atualiza a sessão do Streamlit com os dados do template a ser editado
    st.session_state.nome_template_editar = nome
    st.session_state.texto_template_editar = texto_arquivo
    mudar_pagina('editar_template')