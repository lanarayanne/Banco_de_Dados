import streamlit as st
from ds.plot import plot_price

st.title('Histórico de Cotações')
st.write('Confira o histórico das cotações das empresas.')

ticker = st.sidebar.text_input(
    'Digite o ticker:',
    value = 'AAPL'
)
fig = plot_price(ticker)
st.plotly_chart(fig)