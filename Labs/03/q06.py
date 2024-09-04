file_name = r'questions.txt'

def ask_sentence() -> None:
    with open(file_name, 'w') as f:
        sentence = input('>> ')
        if sentence[-1] == '?':
            f.write(sentence)
            print('write successful')

try:
    ask_sentence()
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('could not read/write file')
except:
    print('unexpected error')
