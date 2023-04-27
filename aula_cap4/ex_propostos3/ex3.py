import numpy as np

arr = np.loadtxt('aula_cap4/files/space.csv', 
                 delimiter=';', 
                 encoding='utf-8', 
                 dtype=str)

cond = np.char.endswith(arr,'USA')

print('Quantidade de missões realizadas pelos EUA =',len(arr[cond]))