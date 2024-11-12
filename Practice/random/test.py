NULL_SET = [None]

def powerset(s):
    power_set = []
    x = len(s)
    for i in range(1 << x):
        power_set.append([s[j] for j in range(x) if (i & (1 << j))])
        if power_set[-1] == []:
            power_set[-1] = NULL_SET

    return sorted(power_set, key=len)

def cartesianproduct(s1, s2):
    return [(x, y) for x in s1 for y in s2]

print(len(powerset([11, 13, 17, 19])))
print(cartesianproduct([1, 2, 4], ['a', 'b', 'c', 'd']))