import numpy as np

arr = np.loadtxt('aula_cap4/files/space.csv', 
                 delimiter=';', 
                 encoding='utf-8', 
                 dtype=str)

arr2 = arr[1:,6].copy()
cond = arr[1:,6].astype(np.float64) > 0

print('média = ',np.mean(arr2[cond].astype(np.float64)))