# enter comma separated values like so: 1,2,3

list1 = input("list1: ").split(',')
list2 = input("list2: ").split(',')

print(dict(zip(list1, list2)))
