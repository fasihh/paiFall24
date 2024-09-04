file_name = r'replacement_needed.txt'

try:
    content = ''
    with open(file_name, 'r+') as f:
        content = f.read()
        print("file:", content)
        content = content.replace(input('before: '), input('after: '))
        f.seek(0)
        f.write(content)
        
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('could not read/write file')
except:
    print('unexpected error')
