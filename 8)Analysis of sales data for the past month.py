import numpy as np
sales_data = np.array([44.50, 15.25, 84.75, 77.00, 5.99, 7.20, 16.75, 11.25])
average_price = np.mean(sales_data)
print(f"The average price of all products sold in the past month is ${average_price:.2f}")
