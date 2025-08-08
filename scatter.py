'''Basic 3D scatter plot
Plot 20 random points in 3D space with different colors for each point.
Hint: Use ax.scatter(x, y, z) in Matplotlib.'''


import matplotlib.pyplot as plt
import numpy as np

# Generate 20 random points (x, y, z) and random colors
x = np.random.rand(21)
y = np.random.rand(21)
z = np.random.rand(21)
colors = np.random.rand(21)
sizes1 = np.random.randint(300, 2000, size=21)

# Create the figure and 3D subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(x, y, z,
                     c=colors,        # color values
                     cmap='cool',     # colormap
                     edgecolors='black',
                     marker='o',
                     s=sizes1,
                     alpha=0.8)


# Labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Basic 3D Scatter Plot')

# Display plot
plt.show() 


'''
import matplotlib.pyplot as plt 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x=np.random.rand(21)
y=np.random.rand(21)
z=np.random.rand(21)
colors=np.random.rand(21)
fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111, projection='3d')
scatter=ax.scatter(x,y,z,c=colors,cmap='cool',edgecolors='black',marker='o',alpha=0.8)
fig.show()
'''