from faker import Faker
import random

fake = Faker()


def generate_fake_user(num_identities):
    for _ in range(num_identities):
        random_number = ''.join(random.sample('0123456789', 9))
        print(fake.email() + ",",
              fake.first_name() + ",",
              fake.last_name() + ",",
              fake.city() + ",",
              fake.country() + ",",
              random_number)


user_input = input('How many identities to create? ')
generate_fake_user(int(user_input))



