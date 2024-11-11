from faker import Faker

def generate_random_email():
    dummy = Faker()
    return dummy.email()
email = generate_random_email()
print(email)
