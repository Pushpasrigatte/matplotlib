import matplotlib.pyplot as plt
x=[1,2,3,4]
y1=[10,20,30,40]
y2=[30,25,20,10]
y3=[2,4,6,8]
plt.subplot(3,1,1)
plt.plot(x,y1)
plt.title("firstplot")
plt.subplot(3,1,2)
plt.plot(x,y2)
plt.title("secondplot")
plt.subplot(3,1,3)
plt.plot(x,y3)
plt.title("thirdplot")
plt.tight_layout()
plt.show()