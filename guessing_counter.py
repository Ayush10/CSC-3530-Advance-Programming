# Program that generates random number and checks it with user guess
# Importing the random library
import random
# Setting the chance as 2 as the index starts from 0
chance = 2
# Declaring sum as a global scope variable
sum = 0
# Notifying the user about the chances they have
print("You have three chances")
print()
# Setting the loop to create 3 (or more) chances
while chance >= 0:
    guess = int(input("Enter a number between 1 and 20 inclusive: "))
    # Generating random number between 1 and 20 because of the question
    number = random.randint(1, 10)
    if guess == number:
        chance = chance + 1
        print("Correct Guess!! You gained one more chance.")
        print("You have %d chances remaining." %(chance + 1))
    else:
        chance = chance - 1
        # Notifying the player about their remaining chances
        print("Incorrect guess!! You have %d chances remaining." %(chance + 1))
    print()
    sum = sum + guess
print()
# Checking the condition according to question
if sum == 25:
    print("Congratulations! You have won the game.")
else:
    print("Sorry you loose the game.")