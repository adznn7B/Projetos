import streamlit as st
from utilidades import *

def pag_configuracao():
    st.markdown('# Configuração')
    email = st.text_input('Digite o seu email:')
    st.button('Salvar', key='salvar_email', on_click=_salvar_email, args=(email, ))
    chave = st.text_input('Digite a chave Gmail:')
    st.button('Salvar', key='salvar_chave', on_click=_salvar_chave, args=(chave, ))
    
def _salvar_email(email):
    pasta_configuracoes.mkdir(exist_ok=True)
    with open(pasta_configuracoes / 'email_usuario.txt', 'w') as f:
        f.write(email)

def _salvar_chave(chave):
    pasta_configuracoes.mkdir(exist_ok=True)
    with open(pasta_configuracoes / 'chave.txt', 'w') as f:
        f.write(chave)

def _le_email_usuario():
    pasta_configuracoes.mkdir(exist_ok=True)
    if (pasta_configuracoes / 'email_usuario.txt').exists():
        with open(pasta_configuracoes / 'email_usuario.txt', 'r') as f:
            return f.read()
    return ''

def _le_chave_usuario():
    pasta_configuracoes.mkdir(exist_ok=True)
    if (pasta_configuracoes / 'chave.txt').exists():
        with open(pasta_configuracoes / 'chave.txt', 'r') as f:
            return f.read()
    return ''