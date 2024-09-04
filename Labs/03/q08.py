try:
    num1, num2 = int(input('num1: ')), int(input('num2: '))
    print(num1/num2)
except ValueError:
    print('incorrect value')
except ZeroDivisionError:
    print('division by zero')
except:
    print('unexpected error')
