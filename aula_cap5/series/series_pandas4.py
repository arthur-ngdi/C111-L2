import pandas as pd

#Condicionais

dic = {'a': 10, 'b': 20, 'c': 30}

series1 = pd.Series(dic)

print(series1[series1 > 15])
