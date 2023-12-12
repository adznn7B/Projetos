# Importando as bibliotecas necessárias.
import streamlit as st
import pandas as pd
from datetime import datetime

# Configurando as informações básicas da página.
st.set_page_config(
    page_title='Jogadores',
    page_icon='🏃',
    layout='wide'
)

# Carregando os dados se ainda não estiverem no estado da sessão.
# Semelhante à página inicial, verificamos se o dataframe já foi carregado para otimizar o desempenho.
if "data" not in st.session_state:
    df_data = pd.read_csv('C:\\Users\\Adriel\\Documents\\GitHub\\Projetos\\Análise de dados da FIFA com Streamlit\\datasets\\CLEAN_FIFA23_official_data.csv', index_col=0)  # Corrigi o caminho para ser relativo.
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data
else:
    df_data = st.session_state['data']

# Extraindo os clubes únicos para o selectbox.
clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)

# Filtrando os jogadores baseado no clube selecionado.
df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].unique()
player = st.sidebar.selectbox('Jogador', players)

# Obtendo as estatísticas do jogador selecionado.
player_stats = df_data[df_data['Name'] == player].iloc[0]

# Exibindo a foto do jogador.
st.image(player_stats['Photo'])

# Exibindo o nome do jogador.
st.title(player_stats['Name'])

# Exibindo informações básicas do jogador.
st.markdown(f'**Clube:** {player_stats["Club"]}')
st.markdown(f'**Posição:** {player_stats["Position"]}')

# Exibindo estatísticas demográficas do jogador em colunas.
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Idade:** {player_stats["Age"]}')
col2.markdown(f'**Altura:** {player_stats["Height(cm.)"] / 100}')  # Convertendo para metros.
col3.markdown(f'**Peso:** {player_stats["Weight(lbs.)"] * 0.453:.2f}')  # Convertendo para kg.
st.divider()

# Exibindo a avaliação geral do jogador e uma barra de progresso.
st.subheader(f'Overall: {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))

# Exibindo informações financeiras do jogador em colunas.
col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Valor de mercado', value=f'£ {player_stats["Value(£)"]:,}')
col2.metric(label='Remuneração semanal', value=f'£ {player_stats["Wage(£)"]:,}')
col3.metric(label='Cláusula de rescisão', value=f'£ {player_stats["Release Clause(£)"]:,}')