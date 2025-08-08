import matplotlib.pyplot as plt
labels=['c','c++','java','python','r','dbms','data science','data structures']
prizes=[300,400,800,900,500,600,700,690]
colors=['red','orange','green','yellow','grey','blue','pink','black']
explode=[0,0,0,0,0,0,0,0.2]
def label_prizes(pct,all_values):
    absolute=int(round(pct/100.*sum(all_values)))
    return f'Rs.{absolute}'
plt.figure(figsize=(8,8))
wedges,texts,autotexts=plt.pie(prizes,labels=labels,colors=colors,autopct=lambda pct:label_prizes(pct,prizes),
                               pctdistance=0.6,explode=explode,startangle=90,textprops={'fontsize':12,'fontweight':'bold','color':'black'})
plt.title("Books Prizes",fontsize=16,fontweight='bold')
plt.axis('equal')
plt.show()