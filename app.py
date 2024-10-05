import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

"""
Criando um Formulário: Use a função st.form 
para criar um formulário. 
Adicione elementos como caixas de texto, botões etc.:


"""

with st.form("user_input_form"):
    name = st.text_input("Nome")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Enviar")

"""
Processando Dados do Formulário: Use os dados coletados do 
formulário para qualquer lógica de negócios necessária:

"""

if submit_button:
    st.write(f"Nome: {name}")
    st.write(f"Email: {email}")


    # Criando dados de exemplo
data = np.random.randn(1000)
# Adicionando um gráfico de barras
st.bar_chart(data)