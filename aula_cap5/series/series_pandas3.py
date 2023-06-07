import pandas as pd

#slicing

dic = {'a': 10, 'b': 20, 'c': 30}

series1 = pd.Series(dic)

print(series1)
print(series1[['b', 'c']])