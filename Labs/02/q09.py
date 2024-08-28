file_name = "test.txt"

with open(file_name, 'r') as f:
    content = " ".join(f.read().split('\n'))
    print("total chars:", len(content))
    print("total words:", len(content.split(' ')))