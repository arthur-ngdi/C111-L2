import numpy as np

np.random.seed(10)

arr = np.random.randint(1,50,16).reshape(4,4)
print(arr)

valores_sem_repeticao, frequencia = np.unique(arr, return_counts=True)

arr2 = np.asarray((valores_sem_repeticao,frequencia)).T
print(arr2)

print(valores_sem_repeticao[frequencia == 2])