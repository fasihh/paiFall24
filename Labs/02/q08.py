conversions = [  
    [1, 1.11, 309.54, 93.25, 160.80], # euro to
    [0.90, 1, 278.62, 83.94, 144.74], # dollar to
    [0.0032, 0.0036, 1, 0.30, 0.52], # pkr to
    [0.011, 0.012, 3.32, 1, 1.72], # inr to
    [0.0062, 0.0069, 1.93, 0.58, 1] # yen to
]

def convert(amount, to_currency, from_currency):
    return amount * conversions[from_currency][to_currency]

amount = float(input("enter amount to be converted: "))
print("currencies available:", "1. euro", "2. dollar", "3. pkr", "4. inr", "5. yen", sep="\n")
from_curr = int(input("enter currency: "))-1
to_curr = int(input("convert to: "))-1

if from_curr >= 5 or from_curr < 0 or to_curr >= 5 or to_curr < 0:
    print("invalid conversion")
else:
    print(convert(amount, to_curr, from_curr))