import re

document = """
    You have a text document that contains dates in various formats such as 12/09/2023, 2023-09-12, and Sep 12, 2023.
    Write a Python script that uses regular expressions to extract all dates in these formats from the text.
"""

dates = re.compile(r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})|(\w{3} \d{1,2}, \d{4})')

[print(date) for group in dates.findall(document) for date in group if date != '']
