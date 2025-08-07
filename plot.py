import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.figure(figsize=(10,6),dpi=100)
plt.plot(x,y,color='red',ls=':',lw=4,marker='o',markerfacecolor='green',markersize=8,markeredgecolor='black')
plt.grid()
plt.show()