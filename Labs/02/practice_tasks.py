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

# string tasks
# task 1
def user_help():
    user_name = input("your good name!\n")
    print("Hello!", user_name)
    choice = input("I hope you are fine, let me know how I can help you!\n")

    if choice == "yes":
        problem = input("share your problem with us\n")
        print("Thanks for your feedback, we will resolve your problem")
        
    print("Okay! Good to see you, stay connected".center(50))
user_help()

# task 2
def get_first_last_name(full_name):
    separated_name = full_name.split(' ')
    return separated_name[0] + " " + separated_name[-1]
print(get_first_last_name("Fasih Hasan Khan"))
    
# output 1
print(calculate_area(8, 1000/11), calculate_area(3, 23))

# output 2
print_greeting()

# output 3
print(find_maximum(1, 2, 3, 5))

# output 4
print(show_info(name="fasih", age=19))
