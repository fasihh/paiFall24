file_name = r'task_3.txt'

list1 = input('list1: ').split(' ')
list2 = input('list2: ').split(' ')

def create_dict():
    try:
        with open(file_name, 'w') as f:
            f.write(str(dict(zip(list1, list2))))
    except FileNotFoundError:
        print('file does not exist')
    except IOError:
        print('could not read/write file')
    except:
        print('unexpected error')
        
if len(list1) == len(list2):
    create_dict()
    print('dictionary created')
else:
    print('list1 and list2 have different lengths')
