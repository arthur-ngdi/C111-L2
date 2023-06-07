import pandas as pd

#Operações

dic = {'a': 10, 'b': 20, 'c': 30}

series1 = pd.Series(dic)
series2 = pd.Series({'a': 10, 'c': 50, 'd': 100})

#Operação de soma entre Series
print(series1 + series2) #hardcode
print(series1.add(series2, fill_value=0)) #pandas
print(series1.sub(series2, fill_value=0)) #pandas
print(series1.mul(series2, fill_value=0)) #pandas
print(series1.div(series2, fill_value=0)) #pandas
