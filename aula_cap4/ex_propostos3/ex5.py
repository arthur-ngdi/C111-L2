import numpy as np

arr = np.loadtxt('aula_cap4/files/space.csv', 
                 delimiter=';', 
                 encoding='utf-8', 
                 dtype=str)

#empresas = arr[0:,1]

empresa, quant_missoes = np.unique(arr[0:,1], return_counts = True)

print(np.stack((empresa,quant_missoes),axis=1)) #a função stack selecionando as colunas (axis=1) junta os dois arrays em uma matriz(x,2)