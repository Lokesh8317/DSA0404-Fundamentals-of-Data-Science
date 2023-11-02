import pandas as pd
data = {
    'customer ID': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'order date': ['2023-07-01', '2022-06-12', '2022-01-03', '2022-08-09', '2020-12-15'],
    'product name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'order quantity': [10, 20, 30, 40, 50]
       }
df = pd.DataFrame(data)
print(df)
orders_per_customer=df.groupby('customer ID').size()
avg_order_quantity_per_product=df.groupby('product  name')['order quantity'].mean()
earliest_order_date=df['order date'].min()
latest_order_date=df['order date'].max()
print(orders_per_customer)
print(avg_order_quantity_per_product)
print("Earliest order Date :",earliest_order_date)
print("Latest order Date :",latest_order_date)
