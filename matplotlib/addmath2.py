import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

data1 = pd.read_csv('D:\\python\\small-python-projects\\matplotlib\\Book1.csv')
x = np.array(data1.Year)
y= np.array(data1.Percentage)
m, b = np.polyfit(x, y, 1)
project = np.array([2020, 2022, 2024, 2025])

plt.xlabel('Year')
plt.ylabel('Percentage Success')
plt.xticks(x[::2])

plt.plot(x,y)
plt.title("Graph showing projected success rates")
plt.plot(x, m*x + b, color='orange', linestyle ='dashed')
plt.plot(project, m*project + b, color='blue', linestyle='dashed')

m2 = round(m, 5)
b2 = round(b, 5)
print("m is ", m2)
print("b is ", b2)







# plt.show()




