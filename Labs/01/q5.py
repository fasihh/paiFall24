n: int = int(input('Enter number of elements in array: '))
int_list: list[int] = []

for i in range(n):
    int_list.append(int(input()))

# delete elements less than x
x: int = int(input('Enter number to delete till: '))

x_i: int = -1
for i in range(n):
    if int_list[i] == x:
        x_i = i
        break

print(int_list[i:])
