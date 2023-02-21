# grade.py
#Author - Niall Wynne
# Taken from Lab 4.1
# A program that reads in a students' percentage
# and prints out the corresponding grade

percentage = float (input ('Enter the percentage: '))

print (percentage)

if percentage < 0 or percentage > 100:
    print ('Please enter a number between 0 and 100')
elif percentage < 40:
    print ('Fail')
elif percentage < 50:
    print ('Pass')
elif percentage < 60:
    print ('Merit 1')
elif percentage < 70:
    print ('Merit 2')
else:
    print ('Distinction')