import matplotlib.pyplot as plt
import numpy as np
import math

x = [0.342, 0.499, 0.643, 0.766, 0.866, 0.940]
y = [i * 1.45 for i in x]

for i in range(6):
    print(x[i], float(np.round(y[i], 2)))
grad = ((y[1]- y[0])/(x[1] -x[0]))
print(grad)



plt.show()