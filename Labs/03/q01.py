file_name = r'task_1.txt'

try:
    with open(file_name, 'r') as f:
        content = f.read()
        print('characters:', len(content))
        print('words:', len(content.split(' ')))
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('could not read/write file')
except:
    print('unexpected error')
