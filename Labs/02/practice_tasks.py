# task 1
def print_greeting():
    print("Hello World!")

# task 2
def calculate_area(length: float, width: float) -> float:
    return length * width

# task 3
def find_maximum(*nums):
    max_val = -float('inf')
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

# task 4
def show_info(**details):
    output = ""
    for detail in details:
        output += f"{detail}: {details[detail]}\n"
    return output
    
# output 1
print(calculate_area(8, 1000/11), calculate_area(3, 23))

# output 2
print_greeting()

# output 3
print(find_maximum(1, 2, 3, 5))

# output 4
print(show_info(name="fasih", age=19))
