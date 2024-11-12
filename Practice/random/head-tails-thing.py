inputs = [1, 0, 0, 0, 0, 1]
n = len(inputs)

current = 0
i = 0
while i < n:
    num = inputs[i]
    current = (current << 1) ^ num
    i += 1

i = 0
combo = 0
while i <= n:
    match (current & 7):
        case 4:
            print(f'head-tail-tail: {i+1} to {i+3}')
            combo += 1
            current >>= 3
            i += 3
        case 1:
            print(f'tail-tail-head: {i+1} to {i+3}')
            combo += 1
            current >>= 3
            i += 3
        case __:
            current >>= 1
            i += 1

if combo // 2 > 0:
    print('double combo found')

