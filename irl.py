import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

gas=pd.read_csv('gas_prices.csv')
plt.figure(figsize=(8,5))
#print(gas)
plt.title('Gas Prices!')
plt.plot(gas.Year, gas.USA,'.-b', label="USA" )
plt.plot(gas.Year, gas.Canada,'.-r' ,label='Canada')
plt.plot(gas.Year, gas['South Korea'], '.-g', label='South Korea')

plt.xticks(gas.Year[::3])
plt.xlabel('Years')
plt.ylabel('US Dollars per Gallon')

plt.legend()
plt.show()