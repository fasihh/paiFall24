def average(temps):
    total = 0
    for temp in temps:
        total += temp
    return total/len(temps)

def highest(temps):
    max_val = -float('inf')
    for temp in temps:
        if temp > max_val:
            max_val = temp
    return max_val

def lowest(temps):
    min_val = float('inf')
    for temp in temps:
        if temp < min_val:
            min_val = temp
    return min_val
    
temps = [32,31,34,31,35,34,25,30,25,25,32,27,25,32,29,25,29,27,30,31,32,28,32,35,32,27,25,29,26,34]
temps.sort()

remove_day = int(input("Enter day to remove: "))-1
if remove_day < 0 or remove_day > 30:
    print("incorrect day")
else:
    temps.pop(remove_day-1)

print("count:", len(temps))
print("average:", average(temps))
print("highest:", highest(temps))
print("lowest:", lowest(temps))
