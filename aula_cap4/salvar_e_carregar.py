import numpy as np

arr = np.loadtxt('aula_cap4/files/space.csv', 
                 delimiter=';', 
                 encoding='utf-8', 
                 dtype=str)
#print(arr[0,:])

#print(arr[1:,1])

print(np.unique(arr[1:,1], return_counts=True))