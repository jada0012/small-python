import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd

x=[0,1,2,3,4,5]
y=[0,2,4,6,8,10]
#rezize
#plt.figure(figsize((7,4), dpi=100);
plt.plot(x,y, label='2x', color='green', linewidth=2, )
#line2
x2=np.arange(0,4,0.5)
plt.plot(x2[:5], x2[:5]**2, 'o-r', label='x^2')
plt.plot(x2[4:], x2[4:]**2, 'o--r')
plt.title('first graph', fontdict={'fontname': 'Comic Sans Ms', 'fontsize': 20})
plt.xlabel('X axis!')
plt.ylabel('Y axis!')
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,3,6,8,10])
plt.legend()
plt.savefig('mygraph.png', dpi=300)

plt.show()
