file_name = r'task_2.txt'

selected = 'X'
replace = 'Fasih'

try:
    with open(file_name, 'r+') as f:
        content = f.read().replace(selected, replace)
        print(content)
        f.seek(0)
        f.write(content)
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('could not read/write file')
except:
    print('unexpected error')
