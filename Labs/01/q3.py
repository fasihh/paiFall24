n: int = int(input('Enter number of items: '))
int_list: list[int] = []

for i in range(n):
    int_list.append(int(input()))

for num in int_list:
    print(num)
