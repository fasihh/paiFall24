file_name = r'task_4.txt'

try:
    with open(file_name, 'w') as f:
        emp_data = [
            input('Name: '),
            input('CNIC: '),
            input('Age: '),
            input('Salary: ')
        ]
        f.write(' '.join(emp_data))
            
    with open(file_name, 'a') as f:
        contact = ' ' + input('Phone #: ')
        f.write(contact)
    print()
        
    with open(file_name, 'r') as f:
        content = f.read().split(' ')
        for i, prop in enumerate(['Name', 'CNIC', 'Age', 'Salary', 'Phone #']):
            print(f'{prop}: {content[i]}')
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('could not read/write file')
except:
    print('unexpected error')
