import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Seed and random data
np.random.seed(5)
data = np.random.randint(1, 100, 50)

# Create histogram bins
hist, bin_edges = np.histogram(data, bins=10)

# Coordinates for 3D bars
x_pos = bin_edges[:-1]             # Left edges of bins
y_pos = np.zeros_like(x_pos)       # All bars start at y=0
z_pos = np.zeros_like(x_pos)       # Bars start from z=0

# Bar dimensions
dx = np.diff(bin_edges)            # Width of each bin
dy = np.ones_like(x_pos) * 5       # Depth (arbitrary constant)
dz = hist                          # Heights = histogram counts

# Create figure
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D histogram bars
ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, 
         color='green', edgecolor='black', alpha=0.8)

# Labels
ax.set_xlabel('Values Range')
ax.set_ylabel('Category')  # Since we made y constant
ax.set_zlabel('Frequency')
ax.set_title("3D Histogram")

plt.show()
