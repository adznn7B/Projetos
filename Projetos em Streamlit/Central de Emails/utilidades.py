# Importação das bibliotecas necessárias
from email.message import EmailMessage
import smtplib
import ssl
import streamlit as st
from pathlib import Path

# Função de inicialização para definir variáveis de estado na sessão do Streamlit
def inicializacao():
    # Define a página central para 'home' se ainda não estiver definida
    if 'pagina_central_email' not in st.session_state:
        st.session_state.pagina_central_email = 'home'
    
    # Inicializa variáveis de estado para destinatários, título e corpo do email
    if 'destinatarios_atual' not in st.session_state:
        st.session_state.destinatarios_atual = ''
    if 'titulo_atual' not in st.session_state:
        st.session_state.titulo_atual = ''
    if 'corpo_atual' not in st.session_state:
        st.session_state.corpo_atual = ''

# Função para enviar emails
def envia_email(email_usuario, destinatarios, titulo, corpo, senha_app):
    # Cria um objeto EmailMessage
    message_email = EmailMessage()
    # Configura o remetente, destinatários e assunto do email
    message_email['From'] = email_usuario
    message_email['To'] = destinatarios
    message_email['Subject'] = titulo
    
    # Define o conteúdo do email
    message_email.set_content(corpo)
    
    # Cria um contexto SSL seguro
    safe = ssl.create_default_context()
    
    # Envia o email usando SMTP sobre SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
        smtp.login(email_usuario, senha_app)
        smtp.sendmail(email_usuario, destinatarios, message_email.as_string())

# Definindo caminhos para pastas de templates, lista de emails e configurações
pasta_atual = Path(__file__).parent
pasta_templates = pasta_atual / 'templates'
pasta_lista = pasta_atual / 'lista_email'
pasta_configuracoes = pasta_atual / 'configuracoes'
    
# Função para mudar a página atual na sessão do Streamlit
def mudar_pagina(nome_pagina):
    st.session_state.pagina_central_email = nome_pagina