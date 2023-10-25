# Importando as bibliotecas necessárias.
import streamlit as st
import webbrowser  # Não está sendo usado, considere removê-lo
import pandas as pd
from datetime import datetime

# Configurando as informações básicas da página.
st.set_page_config(
    page_title='Clubes',
    page_icon='⚽',
    layout='wide'
)

# Carregando os dados se ainda não estiverem no estado da sessão.
# Semelhante à página inicial, verificamos se o dataframe já foi carregado para otimizar o desempenho.
if "data" not in st.session_state:
    df_data = pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)  # Corrigi o caminho para ser relativo.
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data
else:
    df_data = st.session_state['data']

# Obtendo uma lista de clubes únicos do dataset
clubes = df_data['Club'].unique()

# Permitindo ao usuário selecionar um clube na barra lateral
club = st.sidebar.selectbox('Clube', clubes)

# Filtrando os dados do clube selecionado
df_filtered = df_data[(df_data['Club'] == club)].set_index('Name')

# Exibindo o logotipo do clube
st.image(df_filtered.iloc[0]['Club Logo'])

# Exibindo o nome do clube como cabeçalho
st.markdown(f'## {club}')

# Definindo as colunas a serem exibidas no dataframe
columns = [
    "Age",
    "Photo",
    "Flag",
    "Overall",
    "Value(£)",
    "Wage(£)",
    "Joined",
    "Height(cm.)",
    "Weight(lbs.)",
    "Contract Valid Until",
    "Release Clause(£)"
]

# Exibindo o dataframe com configurações personalizadas para algumas colunas
st.dataframe(
    df_filtered[columns],
    column_config={
        'Overall': st.column_config.ProgressColumn(
            'Overall', format='%d', min_value=0, max_value=100
        ),
        'Wage(£)': st.column_config.ProgressColumn(
            'Weekly Wage', format="£%f", min_value=0, max_value=df_filtered['Wage(£)'].max()
        ),
        'Photo': st.column_config.ImageColumn(),
        'Flag': st.column_config.ImageColumn('Country')             
    }
)