# Program to guess random variable
# Importing random library
import random
# Taking user input
number = int(input("Enter your guess number: "))
# Genrating random number between the below range
random_number = random.randint(1, 50)
# Chcecking the guess number
if number == random_number:
    print("Your guess is correct")
    print("The number is : %d" %random_number)
else:
    print("Your guess is incorrect")
    print("The random number is: %d" %random_number)
    print("Your number is: %d" %number)