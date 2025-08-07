import matplotlib.pyplot as plt
students=['a','b','c','d','e']
marks=[77,45,56,80,95]
colors=['red','green','blue','orange','yellow']
bars=plt.bar(students,marks,color=colors,edgecolor='black',lw=3,width=0.5,align='center',hatch='//')
for bar in bars:
    height=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2,height+0.5,str(height),ha='center',fontsize=10)
plt.title("performance bar chart")
plt.xlabel("marks/100")
plt.ylabel("students")
plt.legend()
plt.grid(ls=":",lw=0.8)
plt.gca().set_facecolor('pink')
plt.tight_layout()
plt.show()