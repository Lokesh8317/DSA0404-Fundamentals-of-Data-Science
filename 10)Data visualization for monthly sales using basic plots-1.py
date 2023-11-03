import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperatures = [14.2, 31.5, 15.2, 10.5, 22.1, 26.3, 28.7, 18.2, 21.1, 20.8, 6.4, 12.2]
plt.plot(months, temperatures, marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
