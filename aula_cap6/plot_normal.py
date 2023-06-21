import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
y = x*2
y2 = x*x

plt.plot(x, y, 's--r', x, y2, 'o-.b', linewidth=1, markersize=10)
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.show()
