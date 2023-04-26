import numpy as np

np.random.seed(10)

arr = np.random.randint(50, size = (4,4))

print("média das colunas = ", arr.mean(axis=0))
print("média das linhas = ", arr.mean(axis=1))

print("maior valor das médias das colunas = " , max(arr.mean(axis=0)))
print("maior valor das médias das linhas = " , max(arr.mean(axis=1)))
