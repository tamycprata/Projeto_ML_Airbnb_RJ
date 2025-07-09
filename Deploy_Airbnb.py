import pandas as pd
import streamlit as st
import joblib

# modelo = joblib.load('modelo.joblib')

# Inicialização de todas as variáveis que são´numericas        
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

# Inicialização de todas as variáveis que são´booleanas 
x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

# Inicialização de todas as variáveis que são listas  
x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancelation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }
# Criando a inicialização dos items da lista com 0
dicionario = {}
for item in x_listas:
    for valor in x_listas:
        dicionario[f'{item}_{valor}'] = 0  #Combina a chave com o valor e atribui 0

# Criando os botões numéricos
for item in x_numericos:
    if item == 'latitude' or item == 'longitude':
         valor = st.number_input(f'{item.capitalize()}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item.capitalize()} (R$)', step=0.01, value=0.0, format="%.2f")
    else:
        valor = st.number_input(f'{item.capitalize()}', step=1, value=0)
    x_numericos[item] = valor
    
# Criando os botões booleano    
for item in x_tf:
    valor = st.selectbox(f'{item.capitalize()}', ('Sim', 'Não')) 
    if valor == 'Sim':
        x_item = 1
    else:
        x_item = 0
    
# Criando os botões com listas    
for item in x_listas:
    valor = st.selectbox(f'{item.capitalize()}', x_listas[item])
    dicionario[f'{item}_{valor}'] = 1

# Criando botão para executar a Machine Learning
botao = st.button("Prever valor do Aluguel")

if(botao):
    dicionario.update(x_numericos)
    dicionario.update(x_tf)
    valores 