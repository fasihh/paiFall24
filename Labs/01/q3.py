n: int = int(input('Enter number of items: '))
int_list: list[int] = []

for i in range(n):
    int_list.append(int(input()))

count = 0
for num in int_list:
    if count % 2 == 0:
        count += 1
print('Evens: ', count)
