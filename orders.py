
import random


def generate_order_data(customers, products):
    order_data = []
    statuses = ['pending', 'delivered', 'in transit', 'cancelled', 'returned']
    for i in range(1000):
        order_id = i + 1
        product = random.choice(products)
        customer = random.choice(customers)
        order = {
            'id': order_id,
            'product_id': product['product_id'],
            'customer_id': customer['id'],
            'product_name': product['product_name'],
            'product_price': product['price'],
            'status': random.choice(statuses)
        }
        order_data.append(order)
    return order_data