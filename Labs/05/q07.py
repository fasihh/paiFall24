import re

email_addresses = [
    'fhk.tcs@gmail.com',
    'owais.@yahoo.com',
    'absergmail.com',
    'ali@nu.edu.pk'
]

def find_emails(text):
    return re.finditer(r'\w+(\.\w+)*@\w+(\.\w+)+', text)

text = ' '.join(email_addresses)
print(f"text: {text}")
for email in find_emails(text):
    print(text[email.start():email.end()])