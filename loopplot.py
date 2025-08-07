import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
functions=[(np.sin(x),'sin(x)','blue'),(np.cos(x),'cos(x)','green'),(x**2,'x^2','brown')]
for func,label,color in functions:
    plt.plot(x,func,label=label,color=color)
plt.xlabel('x')
plt.ylabel('y')
plt.title('multiple lines using a loop')
plt.legend()
plt.grid()
plt.show()