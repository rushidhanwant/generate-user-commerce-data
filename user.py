import random

from faker import Faker
def generate_user_data():
    user_data = []
    fake = Faker("en_US")
    for _ in range(1000):
        name = fake.name()
        wallet = random.randint(100, 10000)
        user_id = fake.unique.random_int(min=111111, max=999999)
        user = {
            'name': name,
            'wallet': wallet,
            'id': user_id
        }
        user_data.append(user)
    return user_data
