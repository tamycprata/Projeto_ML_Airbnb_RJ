# 🏠 Previsão de Preço de Aluguel no Airbnb - Rio de Janeiro

Este projeto utiliza **Machine Learning** para prever o valor de aluguel de um imóvel no Airbnb com base em características do anúncio. O modelo foi treinado em dados reais da cidade do **Rio de Janeiro** e disponibilizado via uma interface interativa criada com **Streamlit**.

---

## 🚀 Funcionalidades

- Interface web para entrada dos dados do imóvel
- Previsão do preço de aluguel com base em atributos fornecidos
- Modelo treinado com `XGBoost` otimizado via `scikit-learn`
- Organização das variáveis em: numéricas, booleanas e categóricas
- Experiência interativa e simples para o usuário

---

## 🧠 Tecnologias utilizadas

- `Python`
- `Streamlit`
- `scikit-learn`
- `XGBoost`
- `joblib`
- `pandas`

---

## 🛠 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/projeto-airbnb-rj.git
cd projeto-airbnb-rj
2. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
Se o arquivo requirements.txt não existir, instale manualmente:

bash
Copiar
Editar
pip install streamlit xgboost scikit-learn pandas joblib
3. Execute o app com Streamlit
bash
Copiar
Editar
streamlit run Deploy_Airbnb.py
📥 Entradas do sistema
O app solicita as seguintes informações:

🔢 Variáveis Numéricas:
Latitude, Longitude

Quantidade de hóspedes (accommodates)

Banheiros, Quartos, Camas

Valor por hóspede adicional (extra_people)

Número mínimo de noites (minimum_nights)

Ano e Mês do anúncio

Número de comodidades (n_amenities)

Quantidade de anúncios do host (host_listings_count)

🔘 Variáveis Booleanas:
Host é superhost?

Reserva instantânea disponível?

🔘 Variáveis Categóricas:
Tipo de propriedade (property_type)

Tipo de quarto (room_type)

Política de cancelamento (cancelation_policy)

📦 Saída
Após preencher o formulário e clicar em "Prever valor do Aluguel", o sistema exibe o preço estimado para o imóvel.

📁 Organização
Deploy_Airbnb.py: Código principal do app Streamlit

modelo_xgboost_otimizado.pkl ou .joblib: Arquivo do modelo treinado

ML_Airbnb_Rio.ipynb: Jupyter Notebook com análise exploratória e treinamento

📌 Observações
O modelo atual foi treinado com foco em imóveis localizados no Rio de Janeiro.

Pode ser adaptado para outras cidades ou plataformas com ajustes mínimos nos dados e variáveis.

👩‍💻 Autor
Tamy Prata
🔗 LinkedIn https://www.linkedin.com/in/tamy-cristine/
📧 tamycristine@yahoo.com.br

📜 Licença
Este projeto está licenciado sob a licença MIT.
