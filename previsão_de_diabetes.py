"""###Importando as bibliotecas ✈"""
#Bibliotecas para algoritmo de Machine Learning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Bibliotecas para a métrica de avaliação
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay, classification_report

#Algoritmo
from sklearn.linear_model import LogisticRegression

#Seletor de modelo para transformar em treino e teste
from sklearn.model_selection import train_test_split

"""###Iniciando a análise exploratória dos dados ⭐"""
#Criando o DataFrame do Pandas
df = pd.read_csv('/content/diabetes.csv')

#Plotando o data frame na tela
df.head()

#Descobrindo quantidade de linhas e colunas
df.shape

#Resumindo o data frame
df.describe().T

#Descobrindo como está separada a coluna de target
df['Outcome'].value_counts()

"""###Iniciando o algoritmo de machine learning (Logistic Regression) ✅"""
#Escolha das colunas

X = df.iloc[:,:-1].values #Todas as colunas exceto a ultima que valida se a pessoa está com diabetes ou não.
y = df.iloc[:,-1].values #Fica apenas a coluna com a informação se a pessoa está com diabetes ou não.

#Separa o modelo em treino e teste

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.30, random_state=10)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Treinando o modelo

classificador = LogisticRegression()
classificador.fit(X_train, y_train)

y_pred = classificador.predict(X_test)
y_proba = classificador.predict_proba(X_test)

#Matriz de confusão
cm = confusion_matrix(y_test, y_pred)

#Gráfico para mostrar a matriz de confusão
ConfusionMatrixDisplay.from_predictions(y_test, y_pred, cmap = plt.cm.Blues,
                                        normalize = None, display_labels = ['Não está com diabete', 'Está com diabete'])

#Mostra as % de cada tipo

print(classification_report(y_pred, y_test))

#Mostra a % da acuracidade de acerto e a probabilidade de estar com diabete
print(accuracy_score(y_test, y_pred))

#Mostra a probabilidade em % sobre a pessoa estar com diabete
print(y_proba)

#Inserindo a probabilidade de diabete de cada pessoa na base de dados

probabilidade = pd.DataFrame(y_proba)
df = pd.merge(df.reset_index(), probabilidade, left_index=True, right_index=True)

df.head()

#Renomeando as colunas de probabilidade

df = df.rename({0: '% Não'}, axis = 1)
df = df.rename({1: '% Sim'}, axis = 1)

df.head()
