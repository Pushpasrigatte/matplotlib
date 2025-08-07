import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,8))
ax=fig.add_subplot(111, projection='3d')
x=np.array([1,2,3])
y=np.array([1,2,3])
z=np.zeros(3)
dx= dy=np.ones(3)*0.4
dz= np.array([[5,10,15], [10,5,20], [15,20,5]])

np.random.seed(42)
colors=plt.cm.tab10(np.random.rand(len(x) * len(y)))
color_index=0

for i in range(len(x)):
    for j in range(len(y)):
        ax.bar3d(x[i], y[j],z[i], dx[i], dy[j], dz[i,j], color=colors[color_index],edgecolor='black')
        color_index += 1  
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
ax.set_title('3D-Plot')
ax.view_init(elev=15,azim=60)
plt.grid()
plt.show()




