import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import clipboard





data = pd.read_csv("D:\\python\\small-python-projects\\matplotlib\\funding.csv")
x = np.array(data.YEAR)
y = np.array(data.BUDGET)
m, b = np.polyfit(x, y, 1)
project = np.array([2020, 2021, 2022, 2023, 2024, 2025])

plt.xlabel("Year")
plt.ylabel("Budget(US Millions)")


plt.plot(x,y)
plt.title("Graph Showing Projected Funding Rates")
plt.plot(x, m*x + b, color='orange', linestyle ='dashed')
plt.plot(project, m*project + b, color='blue', linestyle='dashed')



m2 = round(m, 5)
b2 = round(b, 5)
print("m is ", m2)
print("b is ", b2)

for i in range(2020, 2026):




    
    unroundd= i*m + b
    # print(roundd)
    h=round(unroundd, 1)
    clipboard.copy(str(h))
    input()


# plt.show()