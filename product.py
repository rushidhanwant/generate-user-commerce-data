
from faker import Faker

import faker_commerce

fake = Faker("en_US")
fake.add_provider(faker_commerce.Provider)


def generate_product_data():
    product_data = []
    for i in range(1000):
        product_id = fake.unique.random_int(min=0, max=999999)
        product_name = fake.ecommerce_name()
        price = fake.ecommerce_price()
        category = fake.ecommerce_category()
        product = {
            'product_id': product_id,
            'product_name': product_name,
            'price': price,
            'category': category
        }
        product_data.append(product)
    return product_data
