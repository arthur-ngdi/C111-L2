import pandas as pd
import numpy as np

#delete e drop

np.random.seed(10)
df = pd.DataFrame(data = np.random.randint(1, 50, [5, 4]),
                  index = ['A', 'B', 'C', 'D', 'E'],
                  columns = ['X', 'Y', 'Z', 'W'])

