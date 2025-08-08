
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(5)
data= np.random.randint (1,100,50)
plt.hist (data, bins=10, color='green', edgecolor='black')
plt.xlabel('Values Range')
plt.ylabel('equality share')
plt.title("Histogram")

plt.show()