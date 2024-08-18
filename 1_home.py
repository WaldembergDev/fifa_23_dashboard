import pandas as pd
import streamlit as st
import webbrowser
from datetime import datetime

if 'data' not in st.session_state:
    df_data = pd.read_csv(r'C:\Users\berg_\Documents\Projects\fifa_23_streamlit\archive\CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.title('FIFA23 OFFICIAL DATASET!')
btn = st.button('Acesso os dados no Kaggle')

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    '''
    O Conjunto de dados
    de jogadores de futebol de 2023 fornece informações
    abrangentes sobre jogadores de futebol profissionais e seus times.
    '''
)