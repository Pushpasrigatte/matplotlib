
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
data1=np.random.randint(1,100,50) 
data2=np.random.randint(1,100,50)
data3=np.random.randint (1,100,50)
plt.hist(data1, bins=10, alpha=0.5, label='Dataset 1', color= 'darkblue', edgecolor='black')
plt.hist(data2, bins=10, alpha=0.5, label='Dataset 2', color='tomato', edgecolor='black')
plt.hist(data3, bins=10, alpha=0.5, label='Dataset 3', color='lightgreen', edgecolor='black')
plt.xlabel('Values')
plt.ylabel("frequency")
plt.title("Multiple histograms overlapping")
plt.legend()
plt.show()