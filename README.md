Previsão de Preços de Aluguéis do Airbnb no Rio de Janeiro

Descrição do Projeto
Este projeto tem como objetivo construir um modelo de Machine Learning para prever o preço de diárias de imóveis anunciados na plataforma Airbnb, especificamente na cidade do Rio de Janeiro. A ideia é que a ferramenta possa auxiliar tanto os anfitriões (hosts) a precificarem seus imóveis de forma mais competitiva, quanto os viajantes a identificarem se um anúncio possui um valor justo em comparação a outros com características semelhantes.

O desenvolvimento do projeto envolveu diversas etapas, desde a coleta e tratamento dos dados até a construção e avaliação de diferentes modelos de regressão, buscando identificar os fatores que mais impactam no valor final da diária.

Fonte dos Dados
Os dados utilizados neste projeto foram extraídos da plataforma Kaggle e podem ser encontrados no seguinte link: Airbnb Rio de Janeiro Dataset.

As bases de dados contemplam o período de abril de 2018 a maio de 2020, com exceção do mês de junho de 2018, que não possuía dados disponíveis. É importante notar que os dados podem ser atualizados na plataforma, o que pode levar a resultados diferentes dos apresentados neste projeto.

Metodologia
O processo de desenvolvimento do modelo seguiu as seguintes etapas:

1. Coleta e Consolidação dos Dados
Os dados, que estavam divididos em arquivos CSV mensais, foram lidos e consolidados em um único DataFrame do Pandas. Foram adicionadas colunas de "ano" e "mês" para facilitar a análise de sazonalidade.

2. Limpeza e Pré-processamento de Dados
Remoção de Colunas Irrelevantes: Foram excluídas colunas que não agregam valor ao modelo, como IDs, URLs e campos de texto livre (descrições, resumos, etc.).

Tratamento de Valores Ausentes:

Colunas com um volume muito alto de valores nulos (acima de 200.000) foram descartadas.

Linhas que continham valores faltantes em colunas consideradas importantes foram removidas.

Conversão de Tipos de Dados: Colunas que representavam valores monetários, como price e extra_people, foram convertidas de texto (objeto) para o formato numérico (float), após a remoção de caracteres como "$" e ",". Outras colunas numéricas também tiveram seus tipos de dados otimizados para reduzir o uso de memória.

3. Análise Exploratória e Tratamento de Outliers
Foi realizada uma análise de correlação entre as variáveis numéricas para identificar possíveis redundâncias, mas nenhuma correlação forte o suficiente para justificar a exclusão de features foi encontrada.

Foram identificados e removidos outliers em diversas colunas, como price, extra_people, host_listings_count, accommodates, bathrooms, bedrooms e beds. A regra utilizada para a remoção foi a do intervalo interquartil (IQR), excluindo valores abaixo de Q1 - 1.5 * Amplitude e acima de Q3 + 1.5 * Amplitude.

4. Engenharia de Features
Variáveis Categóricas: Colunas de texto como property_type, room_type, bed_type e cancellation_policy foram transformadas em variáveis numéricas através do método de one-hot encoding (get_dummies do Pandas).

Comodidades (amenities): A coluna amenities, que continha uma lista de comodidades em formato de texto, foi transformada em uma coluna numérica que representa a quantidade total de comodidades de cada anúncio.

5. Modelagem e Avaliação
Os dados foram divididos em conjuntos de treino e teste.

Diferentes modelos de regressão foram treinados e avaliados, incluindo:

Regressão Linear

Random Forest Regressor

Extra Trees Regressor

Gradient Boosting Regressor

XGBoost Regressor

LightGBM Regressor

A avaliação dos modelos foi realizada utilizando as métricas R² (Coeficiente de Determinação) e RMSE (Raiz do Erro Quadrático Médio). O modelo com o melhor desempenho em ambas as métricas foi selecionado como o modelo final.

Tecnologias Utilizadas
Pandas: Para manipulação e análise dos dados.

NumPy: Para operações numéricas.

Seaborn e Matplotlib: Para visualização de dados.

Plotly Express: Para criação de gráficos interativos.

Scikit-learn: Para a construção dos modelos de Machine Learning (LinearRegression, RandomForestRegressor, ExtraTreesRegressor, RandomizedSearchCV, GradientBoostingRegressor).

XGBoost e LightGBM: Para a implementação de modelos de Gradient Boosting de alta performance.

Joblib: Para salvar o modelo treinado.

Como Executar o Projeto
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:
(É recomendado criar um ambiente virtual)

Bash

pip install -r requirements.txt
Caso não haja um arquivo requirements.txt, instale as bibliotecas listadas na seção "Tecnologias Utilizadas".

Execute o Notebook:
Abra o Jupyter Notebook e execute o arquivo ML_Airbnb_Rio.ipynb.

Resultados
O projeto resultou em um modelo de previsão de preços com bom desempenho, capaz de auxiliar na precificação de imóveis no Airbnb. A análise das features mais importantes para o modelo revelou que características como a localização, o número de quartos e banheiros, e a quantidade de comodidades oferecidas são fatores determinantes no preço da diária.

Como Contribuir
Contribuições para o aprimoramento deste projeto são bem-vindas. Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.
