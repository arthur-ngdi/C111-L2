import numpy as np

arr = np.array(['Dudu','Paulo','Pedro','Letícia','Daniela'])
cond = np.char.find(arr, 'e')>0

print(arr[cond])
