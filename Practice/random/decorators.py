# keep taking input until valid input

def validate(value):
    def validate_decorator(func):
        def wrapper():
            while func() != value:
                pass
        return wrapper
    return validate_decorator

def user_input(value):
    @validate(value)
    def input_wrapper():
        return int(input('enter: '))
    input_wrapper()

if __name__ == '__main__':
    user_input(int(input('value: ')))
