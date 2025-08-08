''' scatter plot - x,y '''
import matplotlib.pyplot as plt
x=[5,7,8,7,6,9,5,3,4,8]
y=[99,86,87,88,100,86,103,87,94,78]
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("scatter plot")
plt.show()