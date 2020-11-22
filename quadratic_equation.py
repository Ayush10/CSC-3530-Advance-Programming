# Program to calculate x1 and x2 and find the quadratic equation
# Formula: [Quadratic Equation  ax**2 + bx + c = 0]
# d= b**2 - 4*a*c
# x1=(-b - cmath.sqrt(d))/(2*a)
# x2=(-b + cmath.sqrt(d))/(2*a)

# Importing CMath Library
import cmath
# Taking input from the user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
# From formula calculating the value of x1 and x2 using the above
# obtained values from the user
d = b ** 2 - 4 * a * c
x1 = (-b - cmath.sqrt(d)) / (2 * a)
x2 = (-b + cmath.sqrt(d)) / (2 * a)
# Printing the above values using the specified format
print("The value of x1 = {0} and x2 = {1}".format(x1, x2))
