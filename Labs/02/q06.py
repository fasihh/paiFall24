def mult(nums):
    ans = 1
    for num in nums:
        ans *= num
    return ans
print(mult([1, 2, 3, 4]))
