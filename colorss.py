
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import matplotlib.colorbar as colorbar
import matplotlib.colors as mcolors
import numpy as np
students=['Ram', 'Ravi', 'Rahul', 'Rithesh']
marks=[10, 20, 30, 40]
norm = mcolors. Normalize(vmin=min (marks), vmax=max(marks))
cmap=cm.viridis
colors=cmap(norm(marks))
fig,ax=plt.subplots()
bars=ax.bar(students,marks,color=colors,edgecolor='black')
sm=cm.ScalarMappable(cmap=cmap,norm=norm)
sm=set_array([])
cbar=plt.colorbar(sm,ax=ax)
cbar.set_label('marks')
ax.set_title('bar chart with viridis')
ax.set_xlabel('students')
ax.set_ylabel('marks')
plt.show()