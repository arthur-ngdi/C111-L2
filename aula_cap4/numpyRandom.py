import numpy as np

#Numeros aleatorios
#subpacote "random"

np.random.seed(5)

arr = np.random.randint(1,10,10)

np.random.seed(10)

arr2 = np.random.randint(1,10,10)

print(arr)
print(arr2)
print(arr+arr2)
print(arr*arr2)

#media
print(np.mean(arr))

#mediana
print(np.median(arr))

#soma
print(np.sum(arr))

#print(np.unique(arr, return_counts=True))
