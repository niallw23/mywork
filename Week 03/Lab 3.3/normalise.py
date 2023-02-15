# normalise.py
#Author - Niall Wynne
# Lab 3.3
# Program that reads in a string and strips any leading
# or trailing spaces. 
# It also should convert the string to lower case.
#Then it should also output the length of the input and output strings.

rawstring = input('Please enter a string: ')
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len (rawstring)
lengthofnormalised = len (normalisedstring)

print (f'That string normalised is {normalisedstring}')

print (f'We reduced the input string from {lengthofrawstring} to {lengthofnormalised} characters.')