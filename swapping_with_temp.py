# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Variables before swapping")
print(a, b)
# Swapping Algorithm
temp = a
a = b
b = temp
print("Variable after swapping")
print(a, b)