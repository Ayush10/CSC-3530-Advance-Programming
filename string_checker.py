# U = "The quick, brown fox, jumps over, the lazy dog "
# Wap to check if string is starting from a,e,i,o,u or not
# if yes then again check the "T" character is in the string or not.
# if no then take a random value and 
# check if the random value is divisible by 2,3,5 or not.
# Importing the random library
import random
# Instantiating the given string.
# text = "The quick, brown fox, jumps over, the lazy dog "
# text = "Ayush Ojha T"
# Finding the character T in the given string
character = text.find('T')
# Checking the condition
if text[0] == 'a':
    if character == 'T':
        print("Character 'T' is in the string.")
if text[0] == 'e':
    if character == 'T':
        print("Character 'T' is in the string.")
if text[0] == 'i':
    if character == 'T':
        print("Character 'T' is in the string.")
if text[0] == 'o':
    if character == 'T':
        print("Character 'T' is in the string.")
if text[0] == 'u':
    if character == 'T':
        print("Character 'T' is in the string.")
else:
    value = random.randint(1, 10)
    if value % 2 == 0:
        print("Randomly generated value %d is divisible by 2" % value)
    if value % 3 == 0:
        print("Randomly generated value %d is divisible by 3" % value)
    if value % 5 == 0:
        print("Randomly generated value %d is divisible by 5" % value)
