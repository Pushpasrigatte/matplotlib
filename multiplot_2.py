import numpy as np
import matplotlib.pyplot as plt
data=['A', 'B', 'C']
x= np.arange(len(data))
v1 = [5, 10, 15]
v2 = [8, 12, 10]
np.random.seed (42)
colors=plt.cm.tab10(np.random.rand(2))
fig, ax= plt.subplots (figsize=(6,4))
ax.bar(x, v1, label='Dataset 1', color=colors[0], edgecolor='black', alpha=0.8)
ax.bar(x, v2, label='Dataset 2', color=colors [1], edgecolor='black', alpha=0.8)
ax.set_xlabel("Data")
ax.set_ylabel('Values')
ax.set_title('Stacked Bar')
ax.legend()
plt.tight_layout()
plt.show()