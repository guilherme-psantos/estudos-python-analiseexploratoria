# -*- coding: utf-8 -*-
"""Analise_exploratoria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YIpCMRs-hG2EIvogZt3Bfz6H4yDqtWzC
"""

#Importando pandas
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn")

#upload do arquivo
from google.colab import files
arq = files.upload()

#criando o dataframe
df = pd.read_excel("AdventureWorks.xlsx")

#visualizando primeiras linhas
df.head()

#quantidade de linhas e colunas
df.shape

#verificando o tipo de dados
df.dtypes

#Receita Total
df["Valor Venda"].sum()

#Custo Total
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #cria uma coluna para custos

df.head(1)

#custo total
round(df["custo"].sum(),2)

#Achando o Lucro (receita - custo)
df["lucro"] = df["Valor Venda"] - df["custo"]

df.head(1)

#Total Lucro
round(df["lucro"].sum(),2)

#Criando coluna com total de dias para envio do produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

"""** Transforma a string de tempo de envio em números **

"""

#extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

#confirmando que transformou a coluna Tempo_envio
df["Tempo_envio"].dtype

#Media de tempo de envio por marca
df.groupby("Marca")["Tempo_envio"].mean()

"""**Missing Values**"""

#verificando se existe dado faltante
df.isnull().sum()

"""**Lucro por ano e Marca**"""

#agrupando dados por ano e marca
df.groupby([df["Data Venda"].dt.year,"Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
print(lucro_ano)

#Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#criando um grafico de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

#Selecionando apenas o ano de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

#construindo o grafico
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title = "Lucro x Mês 2009")
plt.xlabel("Mês")
plt.ylabel("Lucro");

#grafico por marca
df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro por Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xtics(rotation='horizontal');

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title = "Lucro por Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xtics(rotation='horizontal');

df["Tempo_envio"].describe()

#grafico boxplot
plt.boxplot(df["Tempo_envio"]);

#histrograma
plt.hist(df["Tempo_envio"], edgecolor = "white");

#tempo minimo
df["Tempo_envio"].min()

#tempo maximo
df["Tempo_envio"].max()

#identificando o outlier (discrepância)
df[df["Tempo_envio"] == 20]

df.to_csv("df_vendas_novo.csv", index="False")

