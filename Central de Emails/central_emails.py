import streamlit as st
from utilidades import *
from pagina_templates import *
from pagina_lista_email import *
from pagina_configuracoes import *

# ============== HOME ===============
def home():
    destinatarios_atual = st.session_state.destinatarios_atual
    titulo_atual = st.session_state.titulo_atual
    corpo_atual = st.session_state.corpo_atual
    
    st.markdown('# Central de Emails')
    destinatarios = st.text_input('Destinatários do email:', value=destinatarios_atual)
    titulo = st.text_input('Título do email:', value=titulo_atual)
    corpo = st.text_area('Digite o email:', value=corpo_atual, height=400)
    col1, col2, col3 = st.columns(3)
    col1.button('Enviar email', use_container_width=True, on_click=_enviar_email, args=(destinatarios, titulo, corpo))
    col3.button('Limpar', use_container_width=True, on_click=_limpar)
    
    st.session_state.destinatarios_atual = destinatarios
    st.session_state.titulo_atual = titulo
    st.session_state.corpo_atual = corpo
    
def _limpar():
    st.session_state.destinatarios_atual = ''
    st.session_state.titulo_atual = ''
    st.session_state.corpo_atual = ''
        
def _enviar_email(destinatarios, titulo, corpo):
    destinatarios = destinatarios.replace(' ', '').split(',')
    email_usuario = _le_email_usuario()
    chave = _le_chave_usuario()
    if email_usuario == '':
        st.error('Adicione o email na página de configurações')
    elif chave == '':
        st.error('Adicione a chave na página de configurações')
    else:
        envia_email(email_usuario,
                    destinatarios=destinatarios,
                    titulo=titulo,
                    corpo=corpo,
                    senha_app=chave
                )

# ============= MAIN ================
def main():
    inicializacao()
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