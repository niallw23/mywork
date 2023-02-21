# guess2.py
# author - Niall Wynne
# Lab 4.2 Loops
# Similar to guess1.py - but program will tell user if guess is too high or too low.

number_to_guess = 30

guess = int(input('Please guess a number: '))

while guess != number_to_guess:
    if guess < number_to_guess:
        print ('Too low')
    else:
        print ('Too high') 
    guess = int(input ('Please guess again: '))

print ('Well done! Yes, the number was', number_to_guess)
