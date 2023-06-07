import pandas as pd

#Carregar Dataset

df = pd.read_csv('aula_cap5/paises.csv', delimiter=';')
print(df)

#função head e tail

#print(df.head(5))
#print("--------------------------------------------")
#print(df.tail(5))

#Mostrar colunas

print(df.columns) #mostra quais os nomes das colunas do dataset