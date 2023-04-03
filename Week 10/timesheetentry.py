# Lab work from Week 10
# Looking at objects

class Timesheetentry:
    def __init__ (self, project, start, duration) :
        self.project = project
        self.start = start
        self.duration = duration
    def __str__ (self) :
        return self.project + ':' + str(self.duration)
import datetime as dt

if __name__ == '__main__':
    ts = dt.datetime(2021, 3, 19, 16, 20)
    test = Timesheetentry('Test', ts, 60)
    print (test)