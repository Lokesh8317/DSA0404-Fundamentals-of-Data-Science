import pandas as pd

data = {
    'Property_ID': [1, 2, 3, 4, 5],
    'Location': ['A', 'B', 'A', 'C', 'B'],
    'Number_of_Bedrooms': [3, 4, 5, 3, 6],
    'Area_in_Square_Feet': [1500, 1800, 2200, 1600, 2500],
    'Listing_Price': [250000, 300000, 350000, 220000, 400000]
}

property_data = pd.DataFrame(data)

average_price_by_location = property_data.groupby('Location')['Listing_Price'].mean()

number_of_properties_more_than_four_bedrooms = len(property_data[property_data['Number_of_Bedrooms'] > 4])

property_with_largest_area = property_data[property_data['Area_in_Square_Feet']== property_data['Area_in_Square_Feet'].max()]

print("Average Listing Price by Location:")
print(average_price_by_location)
print("\nNumber of Properties with More than Four Bedrooms:", number_of_properties_more_than_four_bedrooms)
print("\nProperty with the Largest Area:")
print(property_with_largest_area)
