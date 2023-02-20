# iseven.py
# Author - Niall Wynne
# Lab Work - week 04. Lab 4.1
# Program that asks the user to enter a number
# The program will then tell the user if it is odd or even

number = int(input ('Enter an integer: '))

if (number % 2) == 0:
    print (f'{number} is an even number')

else:
    print (f'{number} is an odd number')
    