import streamlit as st

st.set_page_config(
    page_title='players',
    layout='wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[df_data['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Jogador', players)

player_status = df_data[df_data['Name'] == player].iloc[0]

st.image(player_status['Photo'])
st.title(player_status['Name'])

st.markdown(f'**Clube:** {player_status['Club']}')
st.markdown(f'**Posição:** {player_status['Position']}')

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'**Idade:** {player_status['Age']}')

with col2:
    st.markdown(f'**Altura:** {player_status['Height(cm.)']/100} m')

with col3:
    st.markdown(f'**Peso:** {player_status['Weight(lbs.)']*0.453:.2f} kg')

st.divider()

st.subheader(f'Overral {player_status['Overall']}')
st.progress(int(player_status['Overall']))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label='Valor de Mercado', value=f'£ {player_status['Value(£)']:,}')

with col2:
    st.metric(label='Remuneração Semanal', value=f'£ {player_status['Wage(£)']:,}')

with col3:
    st.metric(label='Cláusula de Rescisão', value=f'£ {player_status['Release Clause(£)']:,}')