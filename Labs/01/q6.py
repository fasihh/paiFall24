marks: dict[str, int] = {
    'physics': int(input('Physics: ')),
    'chemistry': int(input('Chemistry: ')),
    'math': int(input('Math: '))
}

max: int = -1
max_subject: str = ''
total: float = 0

for subject in marks:
    value = marks[subject]
    if value > max:
        max = value
        max_subject = subject
    total += value

print('Subject with highest:', max_subject)
print('Average of all subjects:', total/3)
