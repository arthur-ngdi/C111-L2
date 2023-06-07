import pandas as pd
import numpy as np

#slicing

np.random.seed(10)
df = pd.DataFrame(data = np.random.randint(1, 50, [5, 4]),
                  index = ['A', 'B', 'C', 'D', 'E'],
                  columns = ['X', 'Y', 'Z', 'W'])

#print(df)
#print(df['W'])
#print(df[['W', 'A']])

#função loc e iloc

print(df.loc[['A','B'],['X','Y','Z']])
print(df.loc[['A'],['Z']])

print(df.iloc[0:2,0:3])
print(df.iloc[0,2])