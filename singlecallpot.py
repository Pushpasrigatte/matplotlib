import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,'b-',x,y2,'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("multiple linee in single plot call")
plt.legend()
plt.show()
plt.pause(10)