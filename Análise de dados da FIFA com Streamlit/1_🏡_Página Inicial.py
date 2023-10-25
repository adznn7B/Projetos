# Importando as bibliotecas necessárias para o projeto.
import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

# Configurando as informações básicas da página.
st.set_page_config(
    page_title='Página Inicial',
    page_icon='🏡',
    layout='wide'
)

# Verificando se os dados já estão carregados no estado da sessão.
# O objetivo é evitar carregar o dataset toda vez que a página é atualizada.
if "data" not in st.session_state:
    # Carregando o dataset a partir de um caminho local.
    df_data = pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)
    
    # Filtrando os jogadores cujo contrato é válido para o ano atual ou posteriores.
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    
    # Ordenando os jogadores pelo atributo 'Overall'.
    df_data = df_data.sort_values(by='Overall', ascending=False)
    
    # Salvando o dataframe no estado da sessão.
    st.session_state['data'] = df_data
else:
    # Caso os dados já estejam no estado da sessão, apenas atribuímos à variável local.
    df_data = st.session_state['data']

# Título da página.
st.markdown('# FIFA23 OFFICIAL DATASET! ⚽​')

# Link do perfil do desenvolvedor na barra lateral.
st.sidebar.markdown('Desenvolvido por [Adriel Alcântara 😄](https://www.linkedin.com/in/adrielalcantara)')

# Botão para acessar o dataset no Kaggle.
btn = st.button('Acesse os dados no Kaggle')
if btn:
    # Se o botão for clicado, uma nova aba se abrirá com o link do dataset no Kaggle.
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

# Uma breve descrição sobre o conjunto de dados.
st.markdown(
    """
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas, estatísticas de jogo, detalhes do contrato e afiliações de clubes.
    
    Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.
    """
)