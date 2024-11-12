import numpy as np
import re

with open('text.txt') as f:
    lines = f.readlines()

    curr_gpas, curr_chs = np.array([]), np.array([])
    total, ch_t = 0, 0
    for line in lines:
        if len(line.strip()) == 0:
            continue
        
        if '/' in line:
            curr_t = (curr_gpas * curr_chs).sum()
            curr_ch_t = curr_chs.sum()
            total += curr_t
            ch_t += curr_ch_t
            print(curr_t / curr_ch_t)
            curr_gpas, curr_chs = np.array([]), np.array([])
            continue

        comment = re.search('#', line)
        if comment:
            start, end = comment.span()
            line = line[:start]

        cleaned = line.strip()
        if not len(cleaned):
            continue

        ch, gpa = map(float, cleaned.split())
        curr_gpas, curr_chs = np.append(curr_gpas, gpa), np.append(curr_chs, ch)

    print('')
    print(total / ch_t)
