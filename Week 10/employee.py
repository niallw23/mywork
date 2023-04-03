# Lab work week 10
from timesheetentry import *
class Employee:
    timesheets = []

    def __init__ (self, first, last):
        self.first = first
        self.last = last 
    def __str__ (self):
        return self.first + ' ' + self.last
    def logminutes (self, project, minutes):
        now = dt.datetime.now
        timesheetentry = Timesheetentry (project, now, minutes)
        self.timesheets.append(timesheetentry)
    def gettotaltime(self):
        totalminutes = 0
        for ts in self.timesheets:
            totalminutes += ts.duration
        return totalminutes





if __name__ == '__main__':
    test = Employee ('Some', 'One')
    print (test)
    assert ('Some One' == str(test))
    test.logminutes('p1', 30)
    test.logminutes('p1', 60)
    mins = test.gettotaltime()
    print (mins)
    assert( mins == 90)

    print ('All good')


