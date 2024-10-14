import pandas as pd
from sklearn.preprocessing import LabelEncoder # para codificar colunas
from sklearn.model_selection import train_test_split # para treinar o modelo de IA
from sklearn.ensemble import RandomForestClassifier # modelo de IA 'randomForest'
from sklearn.neighbors import KNeighborsClassifier # modelo de IA 'knn'
from sklearn.metrics import accuracy_score

# Lendo a base de dados
tabela = pd.read_csv("clientes.csv")
print(tabela)

# Conferindo as colunas da tabela e se há algum erro na base de dados para ser corrigido
print(tabela.columns)
print(tabela.info())

# Assimilando uma variavel a função de codificação para transformar as colunas de texto em númericas
codificador = LabelEncoder()

# Para cada coluna na lista de colunas da tabela
for coluna in tabela.columns:
    if  tabela[coluna].dtype == 'object' and coluna != 'score_credito': # Se a coluna for de tipo objeto e não for a coluna de score de crédito
        tabela[coluna] = codificador.fit_transform(tabela[coluna]) # Codifica a coluna

print(tabela.info())

# x é a(s) coluna(s) que o modelo de IA vai usar para prever o que queremos
# y é a coluna que queremos advinhar com o modelo de IA
x = tabela.drop(["score_credito", "id_cliente"], axis=1)
y = tabela["score_credito"]

#  Divisão do conjunto de dados em treino e teste. Assim a IA poderá aprender com os dados e testar o que aprendeu para aperfeiçoar
xTreino, xTeste, yTreino, yTeste = train_test_split(x, y) # é possível adicionar outros argumentos para definir a fatia de treino-teste ou definir algumas amneiras de treinamento

# Criando os modelos de IA
modeloRandomForest = RandomForestClassifier()
modeloKnn = KNeighborsClassifier()

# Treinando os modelos
modeloRandomForest.fit(xTreino, yTreino)
modeloKnn.fit(xTreino, yTreino)

# Calculando previsões dos modelos
previsaoRandomForest = modeloRandomForest.predict(xTeste)
previsaoKnn = modeloKnn.predict(xTeste)

# Comparando as previsões obtidas pelo treino com os testes
print(accuracy_score(yTeste, previsaoRandomForest)) # 82,5% de precisão (acurácia)
print(accuracy_score(yTeste, previsaoKnn)) # 74,9% de precisão (acurácia)

# Fazendo previsões com a nova base de dados de clientes
novaTabela = pd.read_csv("novos_clientes.csv")
print(novaTabela)

# Codificando a nova base de dados para a IA conseguir ler
for coluna in novaTabela.columns:
    if novaTabela[coluna].dtype == "object" and coluna != "score_credito":
        novaTabela[coluna] = codificador.fit_transform(novaTabela[coluna])

# Fazendo as previsões com o modelo mais eficiente
novasPrevisoes = modeloRandomForest.predict(novaTabela)
print(novasPrevisoes)

# Descobrindo quais colunas a IA considera mais importante para definir o score de crédito
colunas = list(xTeste.columns)
importancia = pd.DataFrame(index= colunas, data= modeloRandomForest.feature_importances_)
print(importancia * 100)