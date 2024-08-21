marks = float(input('Enter marks: '))

if marks >= 80:
    if marks > 85:
        print('CS-A')
    else:
        print('CS-B')
elif marks >= 70:
    if marks > 75:
        print('AI-A')
    else:
        print('AI-B')
elif marks >= 60:
    if marks > 65:
        print('DS-A')
    else:
        print('DS-B')
else:
    print('Nothing')
