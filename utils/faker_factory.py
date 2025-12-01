import random
from faker import Faker

fake = Faker()

available_countries = [
    "India",
    "United States",
    "Canada",
    "Australia",
    "Israel",
    "New Zealand",
    "Singapore"
]

def fake_new_user():
    return {
        "name": fake.name(),
        "email": fake.email()+"123",
        "password": fake.password(),
        "birthday": {  
            "day": fake.day_of_month(),
            "year": fake.year(),
            "month": fake.month_name(),
        },
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": random.choice(available_countries),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.postcode(),
        "mobile_number": fake.numerify("##########")
    }
    
def fake_contact_form():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "subject": fake.sentence(nb_words=6),
        "message": fake.paragraph(nb_sentences=3)
    }