# How to Build a Number Guessing Game in Python
'''In this project,
you will create a simple number guessing game that allows the user to guess a random number between 1 and 100.
The program will give hints to the user after each guess, indicating whether their guess was too high or too low,
until the user guesses the correct number.'''
import random
secret_number = random.randint(1,101)
print(f"Your secret number is {secret_number}...")
# now guess number from user 
guess = int(input("Enter a random number u want between 1 to 100. "))
# to check whether guess number and secret number matches
if guess == secret_number:
    print("Congraulations!,u guessed the perfect number...")
elif guess < secret_number:
    print("OOPS! u picked lower number than secret number...")
else:
    print("OOPS! u picked greater number than secret number...")