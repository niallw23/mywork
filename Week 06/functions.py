# functions.py
# Author - Niall Wynne
# Works on functions from Lab work in week 06
# The task is to to create a program that allows a user to create new students and to view students.

## Shows how to break your code into smaller, more manageable parts.

def displaymenu ():
    print ('What would you like to do?')
    print ('\t(a) Add new student')
    print ('\t(v) View students')
    print ('\t(q) Quit')
    choice = input('Type one letter - a/v/q :').strip ()

    return choice
def doadd():
    print ('in adding')
def doview ():
    print ('in viewing')

choice = displaymenu ()
while (choice != 'q'):
    if choice == 'a':
        doadd()
    elif choice == 'v':               # using the first function
        doview()
    elif choice != 'q':
        print ('\n\nPlease select either a, v or q')
    choice = displaymenu ()
    
print (f'You chose {choice}')

