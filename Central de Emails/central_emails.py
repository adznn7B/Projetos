import streamlit as st
from pathlib import Path

pasta_atual = Path(__file__).parent
pasta_templates = pasta_atual / 'templates'
pasta_lista = pasta_atual / 'lista_email'

if 'pagina_central_email' not in st.session_state:
    st.session_state.pagina_central_email = 'home'
    
def mudar_pagina(nome_pagina):
    st.session_state.pagina_central_email = nome_pagina
    
def home():
    st.markdown('# Central de Emails')
    
def pag_templates():
    st.markdown('# Templates')
    st.divider()
    for arquivo in pasta_templates.glob('*.txt'):
        nome_arquivo = arquivo.stem.replace('_', ' '). upper()
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(nome_arquivo, key=f'{nome_arquivo}', use_container_width=True)
        col2.button('Editar', key=f'editar_{nome_arquivo}', use_container_width=True, on_click=editar_arquivo, args=(nome_arquivo, ))
        col3.button('Remover', key=f'remover_{nome_arquivo}', use_container_width=True, on_click=remove_template, args=(nome_arquivo, ))
    st.divider()
    st.button('Adicionar Template', on_click=mudar_pagina, args=('adicionar_novo_template',))
    
def pag_adicionar_novo_template(nome_template='', texto_template=''):
    nome_template = st.text_input('Nome do template: ', value=nome_template)
    texto_template = st.text_area('Escreva o texto do template: ', value=texto_template, height=600)
    st.button('Salvar', on_click=salvar_template, args=(nome_template, texto_template))
    
def salvar_template(nome, texto):
    pasta_templates.mkdir(exist_ok=True)
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_templates / nome_arquivo, 'w') as f:
        f.write(texto)
    mudar_pagina('templates')
    
def remove_template(nome):
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    (pasta_templates / nome_arquivo).unlink()
    
def editar_arquivo(nome):
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_templates / nome_arquivo) as f:
        texto_arquivo = f.read()
    st.session_state.nome_template_editar = nome
    st.session_state.texto_template_editar = texto_arquivo
    mudar_pagina('editar_template')
    
def pag_lista_email():
    st.markdown('# Lista de Emails')
    st.divider()
    for arquivo in pasta_lista.glob('*.txt'):
        nome_arquivo = arquivo.stem.replace('_', ' ').upper()
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(nome_arquivo, key=f'{nome_arquivo}', use_container_width=True)
        col2.button('Editar', key=f'editar_{nome_arquivo}', use_container_width=True, on_click=editar_lista, args=(nome_arquivo, ))
        col3.button('Remover', key=f'remover_{nome_arquivo}', use_container_width=True, on_click=remove_lista, args=(nome_arquivo, ))
    st.divider()
    st.button('Adicionar Lista', on_click=mudar_pagina, args=('adicionar_nova_lista',))
    
def pag_adicionar_nova_lista(nome_lista='', emails_lista=''):
    nome_lista = st.text_input('Nome da lista: ', value=nome_lista)
    emails_lista = st.text_area('Escreva os emails separados por vírgula: ',value=emails_lista, height=600)
    st.button('Salvar', on_click=salvar_lista, args=(nome_lista, emails_lista))
    
def salvar_lista(nome, texto):
    pasta_lista.mkdir(exist_ok=True)
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_lista / nome_arquivo, 'w') as f:
        f.write(texto)
    mudar_pagina('lista_emails')
    
def remove_lista(nome):
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    (pasta_lista / nome_arquivo).unlink()

def editar_lista(nome):
    nome_arquivo = nome.replace(' ', '_').lower() + '.txt'
    with open(pasta_lista / nome_arquivo) as f:
        texto_arquivo = f.read()
    st.session_state.nome_lista_editar = nome
    st.session_state.texto_lista_editar = texto_arquivo
    mudar_pagina('editar_lista')

def pag_configuracao():
    st.markdown('# Configuração')
    

def main():
    st.sidebar.button('Central de Emails', use_container_width=True, on_click=mudar_pagina, args=('home',))
    st.sidebar.button('Templates', use_container_width=True, on_click=mudar_pagina, args=('templates',))
    st.sidebar.button('Lista de Emails', use_container_width=True, on_click=mudar_pagina, args=('lista_emails',))
    st.sidebar.button('Configuração', use_container_width=True, on_click=mudar_pagina, args=('configuracao',))

    if st.session_state.pagina_central_email == 'home':
        home()
    elif st.session_state.pagina_central_email == 'templates':
        pag_templates()
    elif st.session_state.pagina_central_email == 'adicionar_novo_template':
        pag_adicionar_novo_template()
    elif st.session_state.pagina_central_email == 'editar_template':
        nome_template_editar = st.session_state.nome_template_editar
        texto_template_editar = st.session_state.texto_template_editar
        pag_adicionar_novo_template(nome_template_editar, texto_template_editar)
    elif st.session_state.pagina_central_email == 'lista_emails':
        pag_lista_email()
    elif st.session_state.pagina_central_email == 'adicionar_nova_lista':
        pag_adicionar_nova_lista()
    elif st.session_state.pagina_central_email == 'editar_lista':
        nome_lista = st.session_state.nome_lista_editar
        texto_lista = st.session_state.texto_lista_editar
        pag_adicionar_nova_lista(nome_lista, texto_lista)
    elif st.session_state.pagina_central_email == 'configuracao':
        pag_configuracao()
            
main()