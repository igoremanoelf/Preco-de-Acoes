import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao[["Close"]]
    return cotacoes_acao

dados = carregar_dados("ITUB4.SA")

#Streamlit 
st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos.
""")

st.write(dados)

# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(dados.index, dados['Close'], marker='o')
plt.title('Evolução do Preço das Ações do Itaú (ITUB4)')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento (R$)')
plt.grid()

# Exibir o gráfico
st.pyplot(plt)
















