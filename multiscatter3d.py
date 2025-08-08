import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(20)
x1=np.random.rand(50)*100
y1=np.random.rand(50)*100
z1=np.random.rand(50)*100
colors1=np.random.rand(50)
sizes1=np.random.randint(50,500,50)

x2=np.random.rand(40)*100
y2=np.random.rand(40)*100
z2=np.random.rand(40)*100
colors2=np.random.rand(40)
sizes2=np.random.randint(40,500,40)

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111, projection='3d')

scatter1=ax.scatter(x1,y1,z1,c=colors1,s=sizes1,cmap='cool',edgecolors='black',marker='o',alpha=0.8,label='Dataset1')
scatter2=ax.scatter(x2,y2,z2,c=colors2,s=sizes2,cmap='viridis',edgecolors='black',marker='*',alpha=0.8,label='Dataset1')

cbar1=fig.colorbar(scatter1,ax=ax,shrink=0.5,pad=0.1)
cbar1.set_label('viridis')

cbar2=fig.colorbar(scatter2,ax=ax,shrink=0.5,pad=0.09)
cbar2.set_label('plasma')

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
plt.title("3-D random scatter plot with 2 DataSets")
plt.legend()
plt.grid()
plt.show()