# 🎬 Projeto de Previsão de Ratings IMDB

Este projeto analisa dados de produções cinematográficas (filmes, séries, espetáculos) e utiliza **Machine Learning** para prever as pontuações do IMDB.  

Foram testados três modelos principais:  
- **DecisionTreeRegressor** (Árvore de Decisão)  
- **TF-IDF + Regressão Linear** (para dados textuais)  
- **LGBMRegressor** (LightGBM - Gradient Boosting)  

O **LightGBM** é o modelo final, usado para fazer a previsão de rating 

---

## 🎯 Resultados do Modelo

### Desempenho do LightGBM:
- **RMSE**: 0.1143  
- **MAE**: 0.0768  
- **R²**: 0.8009  

O modelo explica cerca de **80% da variância** das notas IMDB, com erros baixos, demonstrando ótima capacidade preditiva.  

Estrutura do projeto


├── data/
│   ├── raw/                      # dados brutos
│   └── processed/                # dados tratados
├── models/                       # modelos salvos em pkl
├── src/
│   ├── pproductions_eda_modelo.ipynb    # script de eda/modelagem 
│   └── get_data.py                  # script que pega dados da api 
├── requirements.txt              # dependências
└── README.md

# Instalação e Requisitos

Crie um ambiente virtual e instale as dependências com:  
```bash
pip install -r requirements.txt

# 🎬 Projeto de Previsão de Ratings IMDB

Este projeto analisa dados de produções cinematográficas (filmes, séries, espetáculos) e utiliza **Machine Learning** para prever as pontuações do IMDB.  

Foram testados três modelos principais:  
- **DecisionTreeRegressor** (Árvore de Decisão)  
- **TF-IDF + Regressão Linear** (para dados textuais)  
- **LGBMRegressor** (LightGBM - Gradient Boosting)  

➡️ O **LightGBM** é o modelo final, usado para realizar as previsões de rating.  

---

## 🎯 Resultados do Modelo

### Desempenho do LightGBM:
- **RMSE**: 0.1143  
- **MAE**: 0.0768  
- **R²**: 0.8009  

📌 O modelo explica cerca de **80% da variância** das notas IMDB, com erros baixos, demonstrando excelente capacidade preditiva.  

---

## 📂 Estrutura do Projeto

├── data/
│   ├── raw/                      # dados brutos
│   └── processed/                # dados tratados
├── models/                       # modelos salvos em pkl
├── src/
│   ├── pproductions_eda_modelo.ipynb    # script de eda/modelagem 
│   └── get_data.py                  # script que pega dados da api 
├── requirements.txt              # dependências
└── README.md

# Instalação e Requisitos

Crie um ambiente virtual e instale as dependências com:  
```bash
pip install -r requirements.txt
