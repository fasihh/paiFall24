out_of: int = 30
marks: dict[str, int] = {
    'Subject1': int(input('Subject1: ')),
    'Subject2': int(input('Subject2: ')),
    'Subject3': int(input('Subject3: '))
}

total: float = 0
for subject in marks:
    print(subject, str(marks[subject]/out_of*100) + '%')
    total += marks[subject]

print('Average of all subjects:', str(total/3/out_of*100) + '%')
