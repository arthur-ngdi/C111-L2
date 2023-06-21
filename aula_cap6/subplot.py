import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = x*2
y2 = x*x

#Configuração do primeiro plot
plt.subplot(1,2,1) #numero de linhas = 1, numero de colunas = 2, índice = 1
plt.plot(x, y, 's--r')

#Configuração do primeiro plot
plt.subplot(1,2,2) #numero de linhas = 1, numero de colunas = 2, índice = 2
plt.plot(x, y2, 'o-.b')

plt.show()



