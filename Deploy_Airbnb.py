import pandas as pd
import streamlit as st
import joblib

# Carrega colunas esperadas a partir do dataset original
dados = pd.read_csv('dados.csv', index_col=0) #index_col=0 retira a primeira coluna de indice
colunas = [col for col in dados.columns if col != 'price']# exclui índice e preço

st.title("Previsão de Valor de Aluguel - Airbnb RJ")

# Entradas numéricas
latitude = st.number_input('Latitude', step=0.00001, value=0.0, format="%.5f")
longitude = st.number_input('Longitude', step=0.00001, value=0.0, format="%.5f")
accommodates = st.number_input('Quantas pessoas o imóvel acomoda?', step=1, value=1)
bathrooms = st.number_input('Quantidade de banheiros', step=1, value=1)
bedrooms = st.number_input('Quantidade de quartos', step=1, value=1)
beds = st.number_input('Quantidade de camas', step=1, value=1)
extra_people = st.number_input('Pessoa Extra (R$)', step=0.01, value=0.0, format="%.2f")
minimum_nights = st.number_input('Número mínimo de noites', step=1, value=1)
ano = st.number_input('Ano', step=1, value=2018)
mes = st.number_input('Mês', step=1, min_value=1, max_value=12, value=1)
n_amenities = st.number_input('Número de comodidades (Ex. Wi-fi, ar condicionado, cafeteira, etc)', step=1, value=10)
host_listings_count = st.number_input('O Host possui quantos imoveis anunciados?', step=1, value=1)

# Entradas booleanas
host_is_superhost = st.selectbox('Host é Superhost?', ('Sim', 'Não'))
instant_bookable = st.selectbox('Reserva Instantânea?', ('Sim', 'Não'))

# Traduções para exibição
property_type_map = {
    'Apartamento': 'Apartment',
    'Cama e café': 'Bed and breakfast',
    'Condomínio': 'Condominium',
    'Suíte de hóspedes': 'Guest suite',
    'Casa de hóspedes': 'Guesthouse',
    'Hostel': 'Hostel',
    'Casa': 'House',
    'Loft': 'Loft',
    'Outros': 'Other',
    'Apartamento com serviços': 'Serviced apartment'
}

room_type_map = {
    'Casa/apto inteiro': 'Entire home/apt',
    'Quarto de hotel': 'Hotel room',
    'Quarto privado': 'Private room',
    'Quarto compartilhado': 'Shared room'
}

cancellation_policy_map = {
    'Flexível': 'flexible',
    'Moderada': 'moderate',
    'Rigorosa': 'strict',
    'Rigorosa com 14 dias de carência': 'strict_14_with_grace_period'
}


# Entradas categóricas
property_pt = st.selectbox("Tipo de Propriedade", list(property_type_map.keys()))
room_pt = st.selectbox("Tipo de Quarto", list(room_type_map.keys()))
cancelamento_pt = st.selectbox("Política de Cancelamento", list(cancellation_policy_map.keys()))

# Mapeia para os valores usados no modelo
property_type = property_type_map[property_pt]
room_type = room_type_map[room_pt]
cancellation_policy = cancellation_policy_map[cancelamento_pt]

# Botão de execução da Machine Learning
if st.button("Prever valor do Aluguel"):

    # Dicionário de entrada com variáveis numéricas e booleanas
    entrada = {
        'latitude': latitude,
        'longitude': longitude,
        'accommodates': accommodates,
        'bathrooms': bathrooms,
        'bedrooms': bedrooms,
        'beds': beds,
        'extra_people': extra_people,
        'minimum_nights': minimum_nights,
        'ano': ano,
        'mes': mes,
        'n_amenities': n_amenities,
        'host_listings_count': host_listings_count,
        'host_is_superhost': 1 if host_is_superhost == 'Sim' else 0,
        'instant_bookable': 1 if instant_bookable == 'Sim' else 0
    }

    # Variáveis dummies (One-hot)
    categorias = {
        f'property_type_{property_type}': 1,
        f'room_type_{room_type}': 1,
        f'cancellation_policy_{cancellation_policy}': 1
    }

    # Combina tudo
    entrada.update(categorias)

    # Converte para DataFrame
    valores_x = pd.DataFrame([entrada])

    # Garante que todas as colunas existam
    valores_x = valores_x.reindex(columns=colunas, fill_value=0)

    # Carrega modelo treinado
    modelo = joblib.load('modelo_xgboost_airbnb.pkl')

    # Faz previsão
    valor_previsto = modelo.predict(valores_x)[0]
    st.success(f'Valor estimado do aluguel: R$ {valor_previsto:,.2f}')
