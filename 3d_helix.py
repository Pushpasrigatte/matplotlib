'''3D Line Plot
Plot a 3D helix curve using:
x=cos(t),y=sin(t),z=t
where t ranges from 0 to 4π.'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Needed for 3D plots

# Create t values from 0 to 4π
t = np.linspace(0, 4*np.pi, 100)

# Parametric equations
x = np.cos(t)
y = np.sin(t)
z = t

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the helix
ax.plot(x, y, z, color='blue', linewidth=2)

# Add labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Helix Curve')

plt.show()
