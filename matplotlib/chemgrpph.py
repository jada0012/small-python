import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.array([10,15,20,25,30,35,40,45,50])
y=np.array([63.15,62.93,60.30, 59.61, 61.41, 57.91, 55.42, 51.70, 47.02])
y2 = np.array([0.016, 0.016, 0.017, 0.017, 0.016, 0.017, 0.018, 0.019, 0.021])
m, b = np.polyfit(x, y, 1)
# m, b = np.polyfit(x, y2, 1)

plt.plot(x,y)
# plt.plot(x,y2)
plt.plot(x, m*x +b)
plt.show()