from email.message import EmailMessage
import smtplib
import ssl
import streamlit as st
from pathlib import Path

def inicializacao():
    if 'pagina_central_email' not in st.session_state:
        st.session_state.pagina_central_email = 'home'
    if 'destinatarios_atual' not in st.session_state:
        st.session_state.destinatarios_atual = ''
    if 'titulo_atual' not in st.session_state:
        st.session_state.titulo_atual = ''
    if 'corpo_atual' not in st.session_state:
        st.session_state.corpo_atual = ''

def envia_email(email_usuario, destinatarios, titulo, corpo, senha_app):
    message_email = EmailMessage()
    message_email['From'] = email_usuario
    message_email['To'] = destinatarios
    message_email['Subject'] = titulo
    
    message_email.set_content(corpo)
    safe = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
        smtp.login(email_usuario, senha_app)
        smtp.sendmail(email_usuario, destinatarios, message_email.as_string())

pasta_atual = Path(__file__).parent
pasta_templates = pasta_atual / 'templates'
pasta_lista = pasta_atual / 'lista_email'
pasta_configuracoes = pasta_atual / 'configuracoes'
    
def mudar_pagina(nome_pagina):
    st.session_state.pagina_central_email = nome_pagina

    