import streamlit as st
from mysql.connector import connect
from functions import *

connection = mysql_connection("177.52.160.63", "acidados_adriel", "k4553K0w!", "acidados_datalake-vm")
cursor = connection.cursor()

with st.form(key='my_form'):
    nome = st.text_input(label='Digite seu nome')
    email = st.text_input(label='Digite seu email')
    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    with connection:
        query = "INSERT INTO teste (nometeste, emailteste) VALUES (%s, %s)"
        cursor.execute(query, (nome, email))
        connection.commit()
        connection.close()
        st.success('Dados inseridos com sucesso!')