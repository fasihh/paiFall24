import json

file_name = r'task_5.txt'

user_data = {'Ali': 23,'Saad':24,'Salman':15,'Shams':25,'Sadiq':46,'Hammad':23,'Test':46}

try:
    with open(file_name, 'w') as f:
        json.dump(user_data, f)
    
    with open(file_name, 'r') as f:
        file_data = json.load(f)
        max_age = max(file_data.values())
        
        for person in file_data:
            if file_data[person] == max_age:
                print(person)
        
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('could not read/write file')
except:
    print('unexpected error')
