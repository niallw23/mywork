# div.py
# Author - Niall Wynne
# Lab Work Week 03
# Writing a program that reads in two numbers and divides the first one 
# by the second and give the integer result and the remainder

x= int(input ('Enter the first number: '))
y = int(input ('Enter the number you want to divide by: '))

answer = int(x//y)
remainder = x%y

print (f'{x} divided by {y} is {answer} with the remainder of {remainder}')
