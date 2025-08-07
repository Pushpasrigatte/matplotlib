import matplotlib.pyplot as plt
x=[1,2,3,4]
y1=[10,20,30,40]
y2=[30,25,20,10]
y3=[2,4,6,8]
y4=[9,6,12,20]
plt.subplot(2,2,1)
plt.plot(x,y1,color='red')
plt.title("firstplot")
plt.subplot(2,2,2)
plt.plot(x,y2,color='green')
plt.title("secondplot")
plt.subplot(2,2,3)
plt.plot(x,y3,color="pink")
plt.title("thirdplot")
plt.subplot(2,2,4)
plt.plot(x,y4,color='blue')
plt.title("fourth plot")
plt.tight_layout()
plt.show()