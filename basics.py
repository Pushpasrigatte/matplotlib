''' 
plot()-keywords
color-linecolor-'red'/#fofc
linestyle - line type - '-','--',':',".",'./-.-
linewidth - thickness of the line - 2,3.5,4
marker-symbol-'o','s','^'
marker size - 6,8,9,10............
(markercolor) pacecolor-'yellow'
marker edge color - 'black'
label=legend - line1,line5



plot.title()-plot title(heading)
plot.xlabel,ylabel() axis labels
plt.grid()-background
plt.legend()-menu
plt.figure()-figure size and resolution

'''
import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.plot(x,y,color='red',ls=':',lw=4,marker='o',markerfacecolor='green',markersize=8,markeredgecolor='black')
plt.title("line plot refferal",fontsize=12,ha='center',va='top',fontweight='bold',color='blue')
plt.xlabel("years of working",fontsize=10,fontweight='bold',color='red')
plt.ylabel("profit in millions",fontsize=10,fontweight='bold',color='red')
plt.gca().set_facecolor('#00ffff')
plt.gcf().set_facecolor("pink")
plt.grid(True,linestyle='--',alpha=0.7)
plt.show()


