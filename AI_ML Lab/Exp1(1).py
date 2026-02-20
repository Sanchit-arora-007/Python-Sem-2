import matplotlib.pyplot as plt
sales = [120, 135, 150, 160, 145, 170, 180, 175, 160, 155, 140, 130]
month=["Jan", "Feb", "Mar","April", "May","June","July", "August", "Sep", "Oct", "Nov", "Dec"]
plt.bar(month, sales, label="Monthly Sales")
plt.title("Monthly-sales Bar Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()
