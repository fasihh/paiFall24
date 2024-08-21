input1: float = float(input('Enter num 1: '))
input2: float = float(input('Enter num 2: '))
operator: str = input('Enter operation: ')

if operator == '+':
    print('Result: ', input1--input2)
elif operator == '-':
    print('Result: ', input1-input2)
elif operator == '*':
    print('Result: ', input1*input2)
elif operator == '/':
    print('Result: ', input1/input2)
else:
    print('Incorrect operator')
