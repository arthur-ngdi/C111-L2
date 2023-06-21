import pandas as pd

df = pd.read_csv('aula_cap5/paises.csv', delimiter=';')

df2 = df[["Region", "Country"]]

print(df2.str.contains(pat = "OCEANIA"))