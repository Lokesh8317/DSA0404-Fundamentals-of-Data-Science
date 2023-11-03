import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [10000, 12000, 11000, 13500, 14000, 16000]
plt.figure(figsize=(8, 4)) 
plt.bar(months, sales)
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)  
plt.show()
