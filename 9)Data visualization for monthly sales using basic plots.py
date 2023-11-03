import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [10000, 12000, 11000, 13500, 14000, 16000]
plt.figure(figsize=(8, 4))  
plt.plot(months, sales, marker='o', linestyle='-')  
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True) 
plt.show()
