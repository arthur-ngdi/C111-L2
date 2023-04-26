import numpy as np

np.random.seed(5)

arr = np.random.randn(10)
print(arr)

arr = 100*arr
print(arr)

arr = np.around(arr)
print(arr)


