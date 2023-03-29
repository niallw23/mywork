# Lab Work Week 09
# Author - Niall Wynne
# Work on errors, exceptions, test cases

def fibonacci(number):
    return []

return7 = [0, 1, 1, 2, 3, 5, 8]
return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

assert fibonacci(7) == return7, 'Incorrect return for 7'
assert fibonacci(11) == return11, 'Incorrect return for 11'
assert fibonacci(0) == [], 'Incorrect return for 0'
assert fibonacci(1) == [0], 'Incorrect return value for 1' 

if __name__ == '__main__':
    print('All Good')