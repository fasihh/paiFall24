n: int = int(input('Enter numbers to input: '))
int_list: list[int] = []

max_val: int = -1
for i in range(n):
    int_list.append(int(input()))
    if int_list[i] > max_val:
        max_val = int_list[i]

print('Max value:', max_val)