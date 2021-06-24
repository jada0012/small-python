import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

data1 = pd.read_csv('D:\\python\\small-python-projects\\matplotlib\\Book1.csv')
x = np.array(data1.Year1)
y= np.array(data1.Percentage1)
m, b = np.polyfit(x, y, 1)


plt.xlabel('Year')
plt.ylabel('Percentage Success')

plt.plot(x,y)
plt.plot(x, m*x + b, color='orange', linestyle ='dashed')






plt.show()





