import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfPaises = pd.read_csv('paises.csv', delimiter=';')
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)')

plt.scatter(dfPaises2['Country'], 
            dfPaises2['GDP ($ per capita)'],
            s = dfPaises2['Area (sq. mi.)']/10000 )
plt.show()
