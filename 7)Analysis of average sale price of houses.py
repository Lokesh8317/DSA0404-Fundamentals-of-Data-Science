import numpy as np

bedrooms = np.array([3, 4, 5, 6, 4, 5, 3, 5])
sale_prices = np.array([250000, 300000, 400000, 450000, 320000, 390000, 220000, 380000])

more_than_four_bedrooms = bedrooms > 4

filtered_prices = sale_prices[more_than_four_bedrooms]

average_price_more_than_four_bedrooms = np.mean(filtered_prices)

print("Average Sale Price of Houses with More than Four Bedrooms: $", average_price_more_than_four_bedrooms)
