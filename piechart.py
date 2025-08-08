import matplotlib.pyplot as plt
labels=['apple','oranges','kiwi','banana','avakado','pomogrante','dragon fruit']
prizes=[30,25,35,10,100,50,60]
colors=['red','orange','green','yellow','grey','blue','pink']
# for cutting part (red','orange','green','yellow')
explode=(0,0.2,0,0,0,0,0)
#shadow for 3d like shadow
plt.pie(prizes,labels=labels,colors=colors,startangle=90,
        explode=explode,shadow=True,autopct='%1.1f%%')
plt.title("Fruit prizes")
plt.axis('equal')
plt.legend()
plt.show()