# Lab work week 10

class Employee:
    timesheets = []

    def __init__ (self, first, last):
        self.first = first
        self.last = last 
    def __str__ (self):
        return self.first + ' ' + self.last

if __name__ == '__main__':
    test = Employee ('Some', 'One')
    print (test)
    assert ('Some One' == str(test))

