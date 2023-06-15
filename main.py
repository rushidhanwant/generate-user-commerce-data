import json
import pandas as pd
from orders import generate_order_data
from product import generate_product_data
from user import generate_user_data

user_data = generate_user_data()
pd.read_json(json.dumps(user_data, indent=4)).to_csv('./generated_data/user_data.csv')

product_data = generate_product_data()
pd.read_json(json.dumps(product_data, indent=4)).to_csv('./generated_data/product_data.csv')

orders_data = generate_order_data(user_data, product_data)
pd.read_json(json.dumps(orders_data, indent=4)).to_csv('./generated_data/orders_data.csv')

