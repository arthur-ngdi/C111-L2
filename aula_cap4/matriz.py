import numpy as np

mtz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# print(mtz/10)
# print(mtz*20)

# print(mtz.mean(axis=0)[1]) #axis=0 => colunas
# print(mtz.sum(axis=1)[0]) #axis=1 => linhas

#CONDICIONAIS DO NUMPY

even_mtz = mtz[mtz%2==1]
print(even_mtz)
