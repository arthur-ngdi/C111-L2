import numpy as np

arr = np.loadtxt('aula_cap4/files/space.csv', 
                 delimiter=';', 
                 encoding='utf-8', 
                 dtype=str)

cond = (arr == 'Success')

print((len(arr[cond]) / len(arr[1:,7]))*100, '% das missões tiveram sucesso')