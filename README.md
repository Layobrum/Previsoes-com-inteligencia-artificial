[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Projeto de Previsões de Score de Crédito com Inteligência Artificial

Este projeto utiliza técnicas de Inteligência Artificial para desenvolver um modelo de previsão de score de crédito para clientes de um banco. 
O modelo é treinado com uma base de dados de clientes e utiliza algoritmos de machine learning para prever o score de crédito com base em características como idade, profissão, salário anual, número de contas, número de cartões, juros de empréstimo, entre outros. 
É possível ver uma prévia do script funcionando em `Video demonstrativo.mp4`.

## Arquivos do Projeto

- `algoritmo.txt`: Descrição passo a passo do algoritmo utilizado para as previsões;
- `main.py`: Script principal (em Python) que executa o modelo de previsão;
- `main.ipynb`: Script no Notebook Jupyter que contém o código e os resultados do modelo de previsão;
- `clientes.csv`: Base de dados de clientes utilizada para treinar o modelo de previsão;
- `novos_clientes.csv`: Base de dados de novos clientes para realizar a previsão do score de crédito.

## Requisitos para funcionamento

- Python;
- Bibliotecas: pandas, scikit-learn;
- Extensões: Jupyter Notebook (opcional)

## Uso do programa

- Clone o repositório para o seu computador;
- Instale as bibliotecas necessárias utilizando `pip install pandas scikit-learn`;
- Execute o script `main.py` para gerar o modelo de previsão;
- Abra o notebook `main.ipynb` (caso tenha instalado a extensão *Jupyter*) para visualizar e explorar os resultados ao longo do processo de criação do modelo (opcional).

## Observações

- Este projeto é uma prática de estudo de programação e os dados e situações utilizados não são verdadeiros, respeitando políticas de privacidade;
- Para utilizar o projeto para outras previsões, substitua a base de dados no comando `pd.read_csv()` nos arquivos `main.py` ou `main.ipynb`.
- O modelo de previsão alcançou uma precisão de 82,5% com o algoritmo de Random Forest e 74,9% com o algoritmo de K-Nearest Neighbors para esta base de dados, o que pode mudar em outros casos.

# Créditos

- Este projeto foi criado por Layo "MrBrum" como prática da oficina `Jornada Python` by *Hashtag Treinamentos*, em 09/10/24;
- Se você tiver alguma dúvida ou sugestão, por favor em contato comigo pelo [Linkedin](https://www.linkedin.com/in/layo-brum/).

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
