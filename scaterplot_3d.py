import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(20)
x=np.random.rand(50)*100
y=np.random.rand(50)*100
z=np.random.rand(50)*100
colors=np.random.rand(50)
sizes=np.random.randint(50,500,50)
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
scatter=plt.scatter(x,y,c=colors,s=sizes,cmap='brg',edgecolors='black',alpha=0.8)
fig.colorbar(scatter,ax=ax,label='color scale')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
plt.title("random scatter plot")
plt.show()