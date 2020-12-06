# Program to check if the value is divisible by 4 or 7 or not
# Taking user input
value = int(input("Enter any number"))

# Checking mechanism
if value % 4 == 0:
    print("The inputted value {0} is divisible by 4.".format(value))
elif value % 7 == 0:
    print("The inputted value {0} is divisible by 7.".format(value))
else:
    print("The inputted value {0} is not divisible by 4 or 7.".format(value))
