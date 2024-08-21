n: int = int(input('Enter number of items: '))
int_list: list[int] = []

for i in range(n):
    int_list.append(int(input()))

sum = 0
for num in int_list:
    sum += num

print(sum)
