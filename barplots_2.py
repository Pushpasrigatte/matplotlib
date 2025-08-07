import matplotlib.pyplot as plt
students=['a','b','c','d','e']
marks=[77,45,56,80,95]
plt.bar(students,marks)
plt.title("performance bar chart")
plt.xlabel("marks/100")
plt.ylabel("students")
plt.show()