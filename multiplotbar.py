import matplotlib.pyplot as plt
data=['A', 'B', 'C', 'D']
x= np.arange(len(data))
v1 = [5, 10, 15, 20]
v2 = [8, 12, 10, 18]
v3 = [3, 7, 13, 17]
width= 0.25
x1=x-width
x2= x
x3=x+width
np.random.seed(42)
colors=plt.cm.tab10(np.random.rand(3))
fig, ax= plt.subplots (figsize=(8,6))
ax.bar(x1, v1, width, label='Dataset 1', color=colors[0], edgecolor='black', alpha=0.4)
ax.bar(x2, v2, width, label='Dataset 2', color=colors [1], edgecolor='black', alpha=0.4)
ax.bar(x3, v3, width, label='Dataset 3', color=colors [2], edgecolor='black', alpha=0.4)
ax.set_xlabel('Data', fontsize=12, color= 'darkblue')
ax.set_ylabel('Values', fontsize=12, color= 'darkblue')
ax.set_title("Multiple Bar Graphs")
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()



