"""Module providing functions for manipulating integer lists."""
print('assign6.py')
from gettext import install
import pip

pip install - Faker

from faker import Faker
from pprint import pprint
import random

fake = Faker()

# Create a list of dictionaries, where each dictionary represents a person
customers = []
for i in range(10):
    person = {
        "customer_id": i + 1,
        "name": fake.name(),
        "address": fake.address(),
        "phone_number": fake.phone_number() if random.choice([True, False]) else None,
        "email": fake.email() if random.choice([True, False]) else None
    }
    customers.append(person)

# Challenge 1: Display all keys for the first person in the customers list
if customers:
    first_person_keys = list(customers[0].keys())
    print("Keys for the first person:")
    print(first_person_keys)
else:
    print("No customers found!")

# Challenge 2: Create a new list called missing_data for customers missing email or phone number
missing_data = [customer for customer in customers if not customer.get("email") or not customer.get("phone_number")]
print("\nCustomers missing contact data:")
pprint(missing_data)

# Challenge 3: Calculate and print the percentage of customers missing contact data
total_customers = len(customers)
missing_data_count = len(missing_data)
percentage_missing = (missing_data_count / total_customers) * 100
print(f"\n{percentage_missing:.2f}% of customers are missing contact data.")
