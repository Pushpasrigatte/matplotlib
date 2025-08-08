import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)
x=np.random.rand(50)*100
y=np.random.rand(50)*100
colors=np.random.rand(50)
sizes=np.random.randint(50,500,50)
scatter=plt.scatter(x,y,c=colors,s=sizes,cmap='cool',edgecolors='black',alpha=0.8)
plt.colorbar(scatter,label='color scale')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("random scatter plot")
plt.show()
