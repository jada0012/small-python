import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

data = pd.read_csv('D:\\python\\small-python-projects\\mpl_slur\\tallyval.csv') #opens file
plt.plot(data.Day, data.FSlur, data.RSlur)
plt.show()
# print(data)

