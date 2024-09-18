import re

email_addresses = [
    'fhk@gmail.com',
    'raghib@yahoo.com',
    'retarded.absergmail.com',
    '@@@gmail@gmail.com',
]

def match_valid(email):
    return re.search(r'^[^@][A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z-a-z]+', email)

for email in email_addresses:
    if match_valid(email):
        print(email)