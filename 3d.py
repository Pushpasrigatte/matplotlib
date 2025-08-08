'''3D surface plot
Plot the surface:
3D surface plot
Plot the surface:
z=sin(sqrt(x**2+y**3)
with 
x,y∈[-
5,5].'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create grid of x, y values
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
z=np.sqrt((X**2 + Y**2))
# Compute z = x^2 + y^2
Z = np.sin(z)

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(X, Y, Z, cmap='cool', edgecolor='none', alpha=0.9)

# Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("3D Surface Plot: z = x² + y²")


# Show plot
plt.show()
