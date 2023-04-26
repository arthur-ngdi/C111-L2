import numpy as np

np.random.seed(10)

mtz = np.random.randint(1, 10, 16).reshape(4,4)

print(mtz)

cond = (mtz%2==0)|(mtz%3==0)
print(mtz[cond])