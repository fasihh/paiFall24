from functools import reduce

nums = [3, 1]
x = len(nums)
pnums = [[nums[j] for j in range(x) if i & (1 << j)] for i in range(1, 1 << x)]

max_or = 0
ored = []
for num in pnums:
    curr_or = reduce(lambda a, b: a | b, num)
    max_or = max(max_or, curr_or)
    ored.append(curr_or)
