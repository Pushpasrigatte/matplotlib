import matplotlib.pyplot as plt
students=['a','b','c','d','e']
marks=[77,45,56,80,95]
plt.barh(students,marks)
plt.title("performance bar chart")
plt.xlabel("students")
plt.ylabel("marks/100")
plt.show()